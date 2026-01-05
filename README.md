# NetGuard-AI 🛡️

![Python Version]( https://img.shields.io/badge/python-3.12%2B-blue)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)
![Repo](https://img.shields.io/badge/github-repo-blue?logo=github)

**NetGuard-AI** is a tool for real-time network traffic monitoring using heuristic analysis and a modular architecture for connecting ML models. It was developed as a demonstration of skills in Network Security and information security automation.

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

## 🚀 Key Features
- **Real-time Sniffing:** Capturing IP/TCP packets using the Scapy library.
- **Threat Detection:** Detection of signs of port scanning and use of non-standard ports (backdoors).
- **Security Logging:** Log rotation and saving events in a format suitable for SIEM systems.
- **Extensibility:** Easy connection of classifiers based on PyTorch/TensorFlow.

## 🛠 Tech stack
- **Language:** Python 3.12
- **Networking:** [Scapy](scapy.net)
- **DevOps:** Docker, GitHub Actions (CI/CD)
- **Monitoring:** ELK Stack (integration via logs)

## 📦 Installation and launch

1. Clone the repository:
   ```bash
   git clone github.com
   cd netguard-ai

**Install dependencies:**

```bash
pip install -r requirements.txt

Run the analyzer  (requires administrator rights to access the network interface)

```bash
sudo python main.py --interface eth0
 

## 📈 Roadmap

- Add a payload entropy analysis module (for detecting encrypted control channels).
- Integration with the Telegram Bot API for instant alerts.
- Export data in JSON format for visualization in Grafana.

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



## 🛡️ Disclaimer

**This software is created solely for educational purposes and for use in sanctioned ethical hacking. The author assumes no liability for unauthorized use.**

## 📄 License

Distributed under the MIT License. Details in the LICENSE file.
