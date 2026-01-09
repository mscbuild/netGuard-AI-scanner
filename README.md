# NetGuard-AI 🛡️
![Security Scan](https://github.com/mscbuild/netGuard-AI-scanner/actions/workflows/security.yml/badge.svg) 
![Python Version]( https://img.shields.io/badge/python-3.12%2B-blue)
![License](https://img.shields.io/badge/license-MIT-blue)
![Repo](https://img.shields.io/badge/github-repo-blue?logo=github)
 ![](https://komarev.com/ghpvc/?username=mscbuild) 
 ![](https://img.shields.io/badge/PRs-Welcome-green)
  ![](https://img.shields.io/github/languages/code-size/mscbuild/netGuard-AI-scanner)
![](https://img.shields.io/badge/code%20style-python-green)
![](https://img.shields.io/github/stars/mscbuild)
![](https://img.shields.io/badge/Topic-Github-lighred)

**NetGuard-AI** is a Python-based network traffic monitoring and analysis framework designed to support the detection of anomalous and potentially malicious network behavior. The system combines real-time packet capture with heuristic and AI-assisted analysis techniques to enhance situational awareness and support proactive network security monitoring.

The project emphasizes modularity, extensibility, and clarity of design, making it suitable for research, prototyping, and controlled enterprise or laboratory environments.

## 🏗️ Project structure

~~~bash
netguard-ai/
├── src/
│   ├── __init__.py
│   ├── sniffer.py       # Traffic capture logic
│   └── analyzer.py      # Logic Analysis (heuristic/AI)
├── logs/                # Folder for recording events
├── main.py              # Entry point
├── requirements.txt     # Dependencies
└── README.md            # Documentation
~~~

## 📌 Data Flow Summary
~~~bash
[ Network Interface ]
          ↓
[ Packet Capture Module ]
          ↓
[ Traffic Analysis Module ]
          ↓
[ Event Logging Subsystem ]
~~~


## 🚀 Key Features
- **Real-time Sniffing:** Capturing IP/TCP packets using the Scapy library.
- **Threat Detection:** Detection of signs of port scanning and use of non-standard ports (backdoors).
- **Security Logging:** Log rotation and saving events in a format suitable for SIEM systems.
- **Extensibility:** Easy connection of classifiers based on PyTorch/TensorFlow.

## ⚙️ How It Works

## 1.Packet Capture

- `sniffer.py` listens to network traffic and collects packet data.

## 2.Analysis

- Captured packets are passed to `analyzer.py`

- Detection `logic` evaluates traffic patterns and flags anomalies.

## 3.Logging & Alerts

- Suspicious events are recorded in the `logs/` directory.

- Future versions may include real-time alerts or dashboards.

## 🛠 Tech stack
- **Language:** Python 3.12
- **Networking:** [Scapy](scapy.net)
- **DevOps:** Docker, GitHub Actions (CI/CD)
- **Monitoring:** ELK Stack (integration via logs)

## 📦 Installation and launch

1. Clone the repository:
   ```bash
   git clone github.com/mscbuild/netGuard-AI-scanner.git
   cd netGuard-AI-scanner

**Install dependencies:**
~~~bash
pip install -r requirements.txt
~~~

Run the analyzer  (requires administrator rights to access the network interface)
~~~bash
sudo python main.py --interface eth0
~~~

## 📈 Roadmap

- Add a payload entropy analysis module (for detecting encrypted control channels).
- Integration with the Telegram Bot API for instant alerts.
- Export data in JSON format for visualization in Grafana.

## 🔒 Use Cases

- Network intrusion detection (basic IDS)

- Security research and experimentation

- Learning network traffic analysis and AI-assisted detection

- Monitoring internal or lab networks

  
## 🛡️ Security Audit

The project is regularly checked for vulnerabilities using automated tools:

- Checking with Bandit (Code Analysis)

~~~bash
pip install bandit
bandit -r . -f txt
~~~

- Checking with Snyk (Dependency Analysis and Docker)

~~~bash
snyk test
~~~

Tool	  Status	   Findings
Bandit		      No critical issues. Scapy usage marked as intentional.
Snyk		         0 vulnerabilities in 4 dependencies.

## Intended Applications

- Network security monitoring and intrusion detection research

- Traffic behavior analysis in controlled enterprise or laboratory networks

- Educational use in cybersecurity, networking, and applied AI courses

- Prototyping and evaluation of anomaly detection 

## Future Development Directions

- Integration of supervised and unsupervised machine learning models

- Development of visualization and reporting dashboards

- Real-time alerting and notification mechanisms

- Support for offline analysis using PCAP data

## 🎯 Limitations

- Detection accuracy is dependent on the quality of heuristics and training data (if AI models are used).

- High-throughput environments may require optimization or distributed deployment.

- Encrypted traffic limits the depth of observable information.

## 🛡️ Disclaimer

**This software is created solely for educational purposes and for use in sanctioned ethical hacking. The author assumes no liability for unauthorized use.**

## 📄 License

Distributed under the MIT License. Details in the LICENSE file.
