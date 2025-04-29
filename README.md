# User-Friendly-System-Call-Interface-for-Enhanced-Securityy
# User-Friendly System Call Interface for Enhanced Security

## 🔐 Overview

This project provides a **command-line-based interface** for securely and intuitively managing **system calls**. The tool simplifies system-level operations for users while embedding **security enhancements**, such as **authentication**, **access control**, and **logging**. Designed for system administrators, researchers, and advanced users, it ensures that powerful system functionalities can be accessed safely without directly dealing with complex system-level code.

---

## 🎯 Features

- 🧾 **Simplified System Call Interface**  
  Abstracts low-level system calls (e.g., `open`, `read`, `write`, `exec`) into easy-to-use commands.

- 🔐 **Authentication Mechanism**  
  Password-based login and optional two-factor authentication (2FA) before allowing access to critical operations.

- 🛡️ **Access Control**  
  Role-based permission system to limit access to dangerous or sensitive system calls.

- 📜 **Comprehensive Logging**  
  Every action is logged with user identity, timestamp, system call type, and parameters.

- 🗂️ **Categorized File and Directory Management**  
  Easily list, create, move, or delete files with added safety checks and validations.

- 🧠 **Smart Suggestions**  
  Suggest the correct command or flag when a user makes a syntax mistake.

---

## 🧰 Technologies Used

- **Programming Language**: Python 3 / C (based on version)
- **Operating System**: Linux (Ubuntu/Kali preferred)
- **Security Libraries**: hashlib, pyotp (optional for 2FA)
- **Logging**: Built-in `logging` module

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.x (for Python version)
- Linux-based system
- Root/admin access for full feature set

### ⚙️ Installation

```bash
git clone https://github.com/yourusername/SecureSysCallInterface.git
cd SecureSysCallInterface
chmod +x setup.sh
./setup.sh
