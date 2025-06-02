# tcp_client.py

import socket

host = '127.0.0.1'  # Localhost
port = 9999

# 1. Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect to the server
client.connect((host, port))

# 3. Receive welcome message
msg = client.recv(1024)
print(f"[Server]: {msg.decode()}")

# 4. Send a reply
client.send(b"Thanks for letting me in!\n")

# 5. Close connection
client.close()
