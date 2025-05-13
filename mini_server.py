import socket
from datetime import datetime

# Define the host and port on which the server will listen
HOST = 'localhost'
PORT = 8080

# Helper function to print logs with timestamps for better debugging
def log(message):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

# Start a TCP socket server
# AF_INET: Refers to IPv4 addressing.
# SOCK_STREAM: Specifies TCP (reliable, connection-oriented stream protocol).
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    # Binds the socket to a specific IP (localhost) and port (8080).
    # This tells the OS: "Send any connection request to this IP+Port to me."
    server.bind((HOST, PORT))

    # Starts listening for incoming client connections.
    server.listen()
    log(f"MiniHTTP Server running on {HOST}:{PORT}...")

    # Continuously wait for and handle client connections.
    while True:
        # accept() blocks and waits until a client connects.
        # Returns a new socket (conn) specific to the client and the client address (addr).
        conn, addr = server.accept()
        with conn:
            log(f"Connected by {addr}")
            try:
                # Reads up to 1024 bytes from the client.
                # decode() converts byte data to a string.
                request = conn.recv(1024).decode()

                # Handle empty requests gracefully
                if not request:
                    raise ValueError("Empty request received")

                log(f"Request received:\n{request.strip()}")

                # HTTP requires CRLF (\r\n) line endings — split accordingly
                lines = request.strip().split('\r\n')
                if not lines:
                    raise ValueError("No lines in request")

                # Parse the first line: "GET /path HTTP/1.1"
                parts = lines[0].split()
                if len(parts) < 2:
                    raise ValueError("Malformed request line")

                method, path = parts[0], parts[1]

                # Handle supported and unsupported HTTP methods
                if method != 'GET':
                    # 405 Method Not Allowed for non-GET requests
                    body = "Method Not Allowed."
                    response = (
                        "HTTP/1.1 405 Method Not Allowed\r\n"
                        f"Content-Length: {len(body)}\r\n"
                        "Content-Type: text/plain\r\n"
                        "Allow: GET\r\n"
                        "Connection: close\r\n"
                        "\r\n"
                        f"{body}"
                    )
                # Prepare the HTTP response depending on the path
                elif path == '/hello':
                    # 200 OK response with body "Hello, world!"
                    body = "Hello, world!"
                    response = (
                        "HTTP/1.1 200 OK\r\n"
                        f"Content-Length: {len(body)}\r\n"
                        "Content-Type: text/plain\r\n"
                        "Connection: close\r\n"
                        "\r\n"
                        f"{body}"
                    )
                elif path == '/':
                    # 200 OK response with body "Welcome to MiniHTTP!"
                    body = "Welcome to MiniHTTP!"
                    response = (
                        "HTTP/1.1 200 OK\r\n"
                        f"Content-Length: {len(body)}\r\n"
                        "Content-Type: text/plain\r\n"
                        "Connection: close\r\n"
                        "\r\n"
                        f"{body}"
                    )
                else:
                    # 404 Not Found response if the path is unrecognized
                    body = "Resource not found."
                    response = (
                        "HTTP/1.1 404 Not Found\r\n"
                        f"Content-Length: {len(body)}\r\n"
                        "Content-Type: text/plain\r\n"
                        "Connection: close\r\n"
                        "\r\n"
                        f"{body}"
                    )

            except ValueError as ve:
                # 400 Bad Request response for malformed requests
                log(f"Bad request: {ve}")
                response = (
                    "HTTP/1.1 400 Bad Request\r\n"
                    "Content-Length: 0\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                )

            except Exception as e:
                # 500 Internal Server Error response for unhandled server-side issues
                log(f"Internal server error: {e}")
                response = (
                    "HTTP/1.1 500 Internal Server Error\r\n"
                    "Content-Length: 0\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                )

            # Send the complete HTTP response back to the client
            conn.sendall(response.encode())
