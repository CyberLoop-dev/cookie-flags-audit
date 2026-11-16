<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:#fb7185&height=180&section=header&text=Cookie%20Flags%20Audit&fontSize=42&fontColor=ffffff" alt="Cookie Flags Audit banner"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=fb7185&center=true&vCenter=true&width=650&lines=Review%20cookie%20security%20flags%20locally." alt="Animated project tagline"/></p>
<p align="center">
<img src="https://img.shields.io/github/license/CyberLoop-dev/cookie-flags-audit?style=for-the-badge" alt="License"/>
<img src="https://img.shields.io/github/languages/top/CyberLoop-dev/cookie-flags-audit?style=for-the-badge" alt="Top language"/>
<img src="https://img.shields.io/github/stars/CyberLoop-dev/cookie-flags-audit?style=for-the-badge" alt="Stars"/>
<img src="https://img.shields.io/github/last-commit/CyberLoop-dev/cookie-flags-audit?style=for-the-badge" alt="Last commit"/>
</p>
<p align="center"><img src="./assets/icon.svg" width="150" alt="Cookie Flags Audit illustration"/></p>

## 🚀 Overview

Cookie Flags Audit checks Set-Cookie header lines from a saved response or pasted text. It reports missing browser protections and special requirements for __Host- and __Secure- cookie prefixes without sending data anywhere.

## ✨ Features

- 🍪 Parse multiple Set-Cookie header lines
- 🛡️ Check Secure, HttpOnly, and SameSite attributes
- 🔒 Validate __Host- and __Secure- prefix rules
- 📤 Export findings as readable text or JSON

## 🎬 Demo

~~~bash
python main.py headers.txt
~~~

No hosted service or account is required.

## ⚡ Quick Start

~~~bash
git clone https://github.com/CyberLoop-dev/cookie-flags-audit.git
cd cookie-flags-audit
python main.py --help
~~~

Python 3.10 or newer is recommended.

## 🧰 Tech Stack

- 🐍 Python 3.10+
- 📦 Python standard library only
- 🧪 unittest for tests

## 📁 Folder Structure

~~~text
cookie-flags-audit/
├── assets/icon.svg
├── tests/test_main.py
├── .gitignore
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
└── requirements.txt
~~~

## 🗺️ Roadmap

- [x] 🧩 Working command-line core
- [x] 🧪 Standard-library tests
- [ ] 📊 Optional richer reports
- [ ] 🧰 More edge-case fixtures

## 🤝 Contributing

Issues and pull requests are welcome. Keep changes focused, add tests for new behavior, and use clear commit messages.

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:#fb7185,100:111827&height=110&section=footer" alt="Animated wave footer"/></p>
