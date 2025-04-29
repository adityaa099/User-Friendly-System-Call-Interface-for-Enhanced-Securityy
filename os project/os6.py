# User-Friendly System Call Interface for Enhance security 

import os
import platform
import tkinter as tk
from tkinter import messagebox
import logging
import hashlib

# Setup logging
logging.basicConfig(filename="syscall_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# Secure user database (hashed passwords)
VALID_USERS = {
    "admin": hashlib.sha256("adminpass".encode()).hexdigest(),
    "user": hashlib.sha256("userpass".encode()).hexdigest(),
}

# Define allowed system commands (Prevent unauthorized access)
def get_allowed_commands():
    """Returns OS-appropriate system commands."""
    if platform.system() == "Windows":
        return {
            "List Files": "dir",
            "Check Disk Usage": "wmic logicaldisk get size,freespace,caption",
            "Show Running Processes": "tasklist"
        }
    else:  # Linux/macOS
        return {
            "List Files": "ls -l",
            "Check Disk Usage": "df -h",
            "Show Running Processes": "ps aux"
        }

ALLOWED_COMMANDS = get_allowed_commands()

def log_action(user, action):
    """Logs system call actions for security tracking."""
    logging.info(f"User: {user} - Action: {action}")

def execute_command(command, username):
    """Executes an allowed system command securely."""
    if command in ALLOWED_COMMANDS:
        log_action(username, f"Executed {command}")
        os.system(ALLOWED_COMMANDS[command])  # Run system command
    else:
        messagebox.showerror("Error", " Unauthorized Command!")
        log_action(username, "Attempted unauthorized command")

def authenticate():
    """Handles user authentication before allowing access to system calls."""
    username = user_entry.get()
    password = pass_entry.get()

    if username in VALID_USERS and hashlib.sha256(password.encode()).hexdigest() == VALID_USERS[username]:
        messagebox.showinfo("Login Successful", f" Welcome, {username}")
        log_action(username, "Logged in successfully")
        root.destroy()  # Close login window
        create_syscall_interface(username)  # Open secure system call interface
    else:
        messagebox.showerror("Login Failed", " Invalid Credentials")
        log_action(username, "Failed login attempt")

def create_syscall_interface(username):
    """Creates the GUI interface for executing secure system calls."""
    syscall_window = tk.Tk()
    syscall_window.title("Secure System Call Interface")

    tk.Label(syscall_window, text=f" Secure System Interface", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Label(syscall_window, text=f"Welcome, {username}", font=("Arial", 10)).pack(pady=5)

    # Buttons for system calls
    for cmd_name in ALLOWED_COMMANDS.keys():
        tk.Button(syscall_window, text=cmd_name, command=lambda c=cmd_name: execute_command(c, username)).pack(pady=5)

    tk.Button(syscall_window, text="Exit", command=syscall_window.destroy).pack(pady=10)

    syscall_window.mainloop()

# Create Login UI
root = tk.Tk()
root.title("Secure System Interface Login")

tk.Label(root, text=" Username:", font=("Arial", 10)).pack(pady=5)
user_entry = tk.Entry(root)
user_entry.pack()

tk.Label(root, text=" Password:", font=("Arial", 10)).pack(pady=5)
pass_entry = tk.Entry(root, show="*")
pass_entry.pack()

tk.Button(root, text="Login", command=authenticate).pack(pady=10)

root.mainloop()
