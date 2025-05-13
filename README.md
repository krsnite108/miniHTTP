# MiniHTTP – A Tiny HTTP Server & Client Built from Scratch

Welcome to **MiniHTTP** – a simple and educational project where I've attempted to build a basic HTTP server and client in pure Python using sockets.

> This project helps you understand how the web works at the protocol level without any web frameworks!

---

## 🔧 What is This?

MiniHTTP is a tiny HTTP server that listens on `localhost:8080` and handles very basic HTTP requests like `GET /` and `GET /hello`. It also includes a client that sends raw HTTP requests to the server and prints the response.

This is a **learning project** to help you understand:

- How HTTP requests and responses work under the hood
- How sockets are used to communicate over a network
- The structure of an HTTP message

---

## 📁 Project Structure

MiniHTTP/
├── mini_http_server.py # The custom HTTP server
├── mini_http_client.py # The raw socket-based client
└── README.md # You're reading it!


---

## ▶️ How It Works \?

### 🖥️ Server (`mini_server.py`)

- Starts a socket on `localhost:8080`
- Waits for incoming connections
- Reads the request line (e.g., `GET /hello HTTP/1.1`)
- Sends back a response like:
  - `Hello, world!` if the path is `/hello`
  - `Welcome to MiniHTTP!` if the path is `/`
  - `404 Not Found` for anything else
  - `405 Method Not Allowed` for non-GET requests
- Closes the connection after responding

### 🌐 Client (`mini__client.py`)

- Connects to the same `localhost:8080`
- Sends a raw `GET` request to a path (like `/hello`)
- Waits for the server’s reply
- Prints the full HTTP response (headers + body)

---

## 📦 How to Run

### 🐍 Requirements
Just Python! No external libraries needed.

### 🟢 Start the Server

```
python mini_http_server.py

You should see something like:
```
❯ python3 mini_server.py
[2025-05-12 03:39:14] MiniHTTP Server running on localhost:8080...
```
🟣 Run the Client (in a new terminal)
```
python mini_http_client.py
You’ll see the full response from the server printed in your terminal.
```
❯ python3 mini_client.py
Connected to localhost:8080
Request sent:
GET /hello HTTP/1.1
Host: localhost
Connection: close


Response received:
HTTP/1.1 200 OK
Content-Length: 13
Content-Type: text/plain
Connection: close

Hello, world!
