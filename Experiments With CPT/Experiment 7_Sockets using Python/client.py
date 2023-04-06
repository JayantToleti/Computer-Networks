#Jayant Toleti
#21117


import socket

# Create a socket object
s = socket.socket()

# Define the host and port to connect to
host = 'localhost'
port = 12345

# Connect to the host and port
s.connect((host, port))

# Define the file to send
filename = 'file.txt'

# Open the file and read its contents
with open(filename, 'rb') as f:
    data = f.read()

# Send the file contents
s.sendall(data)

# Close the socket connection
s.close()
