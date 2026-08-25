#!/usr/bin/env python3

#This script parses the Snort logs, determines attacked target, and scales down resources 

import pyparsing as pyp
import itertools
import subprocess

tStamp1 = subprocess.getoutput('date +%m/%d-%H:%M')

# Services Running on Cluster and the IP Configuration

tomcat = "10.2.6.145:80"
mongodb = "10.2.126.3:27017"
wordpress = "10.2.105.99:80"

integer = pyp.Word(pyp.nums)
ip_addr = pyp.Combine(integer+'.'+integer+'.'+integer+'.'+integer+':'+integer)

def snort_parse(logfile):
  header = (pyp.Suppress("[**] [") + pyp.Combine(integer + ":" + integer + ":" + integer) + pyp.Suppress(pyp.SkipTo("[**]", include = True)))
    pri = pyp.Suppress("[Priority:") + integer + pyp.Suppress("]")
    date = pyp.Combine(integer+"/"+integer+'-'+integer+':'+integer+':'+integer+'.'+integer)
    src_ip = ip_addr + pyp.Suppress("->")
    dest_ip = ip_addr

    bnf = header+pri+date+src_ip+dest_ip

    with open(logfile) as snort_logfile:
        for has_content, grp in itertools.groupby(
                snort_logfile, key = lambda x: bool(x.strip())):
            if has_content:
                tmpStr = ''.join(grp)
                fields = bnf.searchString(tmpStr)
                try:
                    if fields[0][2] >= tStamp1:
                        if fields[0][4] == tomcat:
#                            print("tomcat-attacked")
                            subprocess.run('ssh k8s-admin@10.0.0.131 "kubectl scale deployment tomcat -n kube-tomcat --replicas=1"', shell=True, check=True, text=True)
                        elif fields[0][4] == mongodb:
#                            print("mongodb-attacked")
                            subprocess.run('ssh k8s-admin@10.0.0.131 "kubectl scale deployment mongodb -n kube-mongodb --replicas=1"', shell=True, check=True, text=True)
                        elif fields[0][4] == wordpress:
#                            print("wordpress-attacked")
                            subprocess.run('ssh k8s-admin@10.0.0.131 "kubectl scale deployment wordpress --replicas=1"', shell=True, check=True, text=True)
                except KeyError:
                    exit
                except IndexError:
                    exit
snort_parse('/var/log/snort/alert')
