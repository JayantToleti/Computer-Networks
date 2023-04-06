#Jayant Toleti
#21117


import socket

# Create a socket object
s = socket.socket()

# Define the host and port to bind to
host = 'localhost'
port = 12345

# Bind the socket to the host and port
s.bind((host, port))

# Listen for incoming connections
s.listen(5)

# Accept a connection
conn, addr = s.accept()
print(f"Connection from {addr} has been established.")

# Define the file to save the received data
filename = 'received_file.txt'

# Receive the file data
with open(filename, 'wb') as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

# Close the connection and socket
conn.close()
s.close()
