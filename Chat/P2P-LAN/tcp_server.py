# tcp_server.py

import socket

host = '0.0.0.0'  # Listen on all interfaces
port = 9999

# 1. Create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind it to the host and port
server.bind((host, port))

# 3. Start listening for connections
server.listen(1)
print(f"[+] Listening on {host}:{port}...")

# 4. Accept a connection
client_socket, address = server.accept()
print(f"[+] Accepted connection from {address}")

# 5. Send a welcome message
client_socket.send(b"Hello! You are connected.\n")

# 6. Receive data from client
data = client_socket.recv(1024).decode()
print(f"[Client]: {data}")

# 7. Close connection
client_socket.close()
server.close()
