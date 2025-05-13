import socket

# Defining the server we want to connect to
HOST = 'localhost'  # This must match the server's HOST
PORT = 8080         # This must match the server's PORT

# Path to request (e.g., '/', '/hello', or something invalid like '/bad')
PATH = '/hello'

# Creating a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    
    # Connecting to the server
    client.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")

    # Creating and sending a simple HTTP GET request
    request = (
        f"GET {PATH} HTTP/1.1\r\n"
        f"Host: {HOST}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    client.sendall(request.encode())
    print("Request sent:")
    print(request)

    # Receiving and printing the full response
    response = b""
    while True:
        part = client.recv(1024)
        if not part:
            break
        response += part

    print("Response received:")
    print(response.decode())
