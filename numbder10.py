import socket
import threading


# Server function
def start_server(host, port):
    """Starts the server, listens for incoming connections, and sends a message."""
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}...")

        while True:
            conn, addr = server_socket.accept()
            print(f"Connection established with {addr}")
            message = "Hello from server!"
            conn.sendall(message.encode())  # Send message to client
            conn.close()  # Close the connection
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()


# Client function
def connect_to_server(host, port):
    """Connects to the server and receives the message."""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        message = client_socket.recv(1024).decode()  # Receive the message
        print("Received from server:", message)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()


# Run the server in a separate thread to allow the client to connect
def run_server():
    server_thread = threading.Thread(target=start_server, args=('127.0.0.1', 65432))
    server_thread.daemon = True  # Daemonize thread to allow it to exit when the main program exits
    server_thread.start()


# Run the client
def run_client():
    connect_to_server('127.0.0.1', 65432)


if __name__ == "__main__":
    # Run server and client
    run_server()
    # Give the server some time to start before the client connects
    import time

    time.sleep(1)
    run_client()
