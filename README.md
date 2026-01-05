# NetGuard-AI 🛡️

![Python Version](img.shields.io/badge/python-3.12%2B-blue)
![License](img.shields.io)
![Status](img.shields.io)

**NetGuard-AI** is a tool for real-time network traffic monitoring using heuristic analysis and a modular architecture for connecting ML models. It was developed as a demonstration of skills in Network Security and information security automation.

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

## 📈 Roadmap

- Add a payload entropy analysis module (for detecting encrypted control channels).
- Integration with the Telegram Bot API for instant alerts.
- Export data in JSON format for visualization in Grafana.

##🛡️ Disclaimer

**This software is created solely for educational purposes and for use in sanctioned ethical hacking. The author assumes no liability for unauthorized use.**

## 📄 License

Distributed under the MIT License. Details in the LICENSE file.
