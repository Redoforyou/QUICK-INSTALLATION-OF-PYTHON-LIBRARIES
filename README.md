# QUICK-INSTALLATION-OF-PYTHON-LIBRARIES
With this program, you can easily download all the necessary libraries for Python if you are a Linux user.

A lightweight, interactive CLI tool designed for Linux developers to quickly set up their Python environment. This tool is specifically optimized for Arch Linux, CachyOS, and other distributions enforcing PEP 668 (External Environment Protection).

🛠 Project Overview
Modern Linux distributions prevent pip from installing packages globally to protect the system's integrity, often resulting in the externally-managed-environment error. This script automates the installation process by utilizing the --break-system-packages flag, allowing you to install essential libraries directly to your system Python without manual flag typing or complex virtual environment setups.

✨ Key Features
PEP 668 Bypass: Automatically handles "externally managed environment" restrictions.
Zero Dependencies: Built strictly with Python standard libraries (subprocess, os, sys). No external installs required to run the script.
Clean UI: A color-coded terminal interface using ANSI escape sequences for a polished look.
Dual Language: Full interactive support for both English and Russian languages.
Smart Search: Suggests common naming conventions (e.g., python-name, pyname) when searching for packages to ensure successful installations.

🚀 Quick Start
To get started, clone the repository and run the main script:

```bash
git clone [https://github.com/Redoforyou/QUICK-INSTALLATION-OF-PYTHON-LIBRARIES.git]([https://github.com/your-username/linux-lib-installer.git](https://github.com/Redoforyou/QUICK-INSTALLATION-OF-PYTHON-LIBRARIES.git))
cd QUICK-INSTALLATION-OF-PYTHON-LIBRARIES
python main.py
