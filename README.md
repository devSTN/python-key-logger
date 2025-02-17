# Remote Keylogger Project

**Disclaimer:**  
This project is intended for **educational purposes only**. You must have explicit permission to install and use this tool on any system. Unauthorized use is **illegal** and **unethical**. The author is not responsible for any misuse or damage caused by this software.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Legal & Ethical Notice](#legal--ethical-notice)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
  - [Attacker (Receiver) Setup](#attacker-receiver-setup)
  - [Victim (Sender) Setup](#victim-sender-setup)
- [Usage Instructions](#usage-instructions)
- [Project Structure](#project-structure)
- [License](#license)
- [Disclaimer](#disclaimer)

---

## Overview

This project demonstrates a **remote keylogger** that captures keystrokes on a victim machine and sends them in real time to an attacker machine. The project is divided into two parts:

1. **Attacker (Receiver) Script:**  
   Listens on a specified network port and prints incoming keystroke logs to the terminal.

2. **Victim (Sender) Script:**  
   Captures keystrokes using the `pynput` library and sends them over a network socket to the attacker machine.

---

## Features

- **Real-time Keystroke Capture:** Logs keystrokes as they are typed.
- **Remote Transmission:** Sends keystroke logs over a network socket.
- **Live Terminal Output on Attacker Machine:** See keystroke logs instantly on the attacker's terminal.
- **Educational Use:** Demonstrates basic network communication and keystroke logging.

---

## Legal & Ethical Notice

- **For Educational Purposes Only:**  
  This tool is intended for learning about cybersecurity and should be used **only** in controlled environments (e.g., on your own systems or where you have explicit permission).

- **Responsible Use:**  
  The use of keyloggers is subject to local laws and regulations. Ensure you are aware of and comply with all applicable laws before using this tool.

- **No Liability:**  
  The author assumes no responsibility for any misuse or damage caused by this software.

---

## Requirements

- **Python 3.6+**
- **Libraries:**
  - `pynput`  
  - No additional external libraries are required for the attacker server script.
- **Network:**  
  Ensure both the attacker and victim machines are on the same network or are routable to each other.

---

## Installation & Setup

### Attacker (Receiver) Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/remote-keylogger.git
   cd remote-keylogger
