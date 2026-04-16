### K8s-SOAR: Automated DDoS Mitigation & Resilience for Kubernetes
Objective
To design and implement a self-healing security architecture within a Kubernetes cluster capable of detecting and mitigating Distributed Denial of Service (DDoS) attacks in real-time. This project leverages Prometheus/Grafana for anomaly detection and automated Python/Go scripts (the SOAR layer) to dynamically update Network Policies and Horizontal Pod Autoscaling (HPA) parameters, ensuring high availability under duress.

The "SOAR" Logic Flow
This project simulates a SOC Analyst's decision-making process through automation:
Detection (The Sensor): Prometheus monitors metrics like container_network_receive_packets_total and HTTP 5xx error rates.
Analysis (The Logic): An Alertmanager trigger or a Python "Watcher" script detects a deviation from the baseline (e.g., 10x traffic spike).
Response (The SOAR Action):
Isolation: The script automatically applies a deny-all NetworkPolicy to the targeted namespace's non-essential ingress.
Rate Limiting: Updates Nginx Ingress annotations to enforce strict request-per-second limits.
Protection: Adjusts the HPA (Horizontal Pod Autoscaler) maximum limit to prevent "Wallet Exhaustion" (EDoS).

Key Technical Components
Component
Role in Project
Security Outcome
NetworkPolicies
Layer 3/4 Firewall
Granular segmentation and instantaneous traffic blocking.
Ingress-Nginx
Layer 7 Protection
Implementation of rate-limiting and WAF-like rules.
Prometheus/KQL
Monitoring Engine
Real-time observability and threat detection.
Python / Shell
SOAR Orchestrator
The "Brain" that executes kubectl commands based on alerts.


SecOps Evidence (The Portfolio "Gold")
The "Attack Simulation": Documentation of using a tool like Locust or hping3 to simulate the DDoS.
The "Recovery" Graph: A Grafana screenshot showing the traffic spike, followed by the "Response" trigger, and the subsequent stabilization of the cluster.
The YAML Artifacts: Clean, well-commented Kubernetes manifests for the "Hardened" environment.

