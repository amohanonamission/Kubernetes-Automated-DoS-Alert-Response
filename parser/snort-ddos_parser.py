#!/usr/bin/env python3

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
  header = (pyp.Suppress("[**] [") + pyp.Combine())










snort_parse('/var/log/snort/alert')
