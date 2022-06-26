from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)  # Prepare a sever socket

# Fill in start
serverPort = 6789
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
# Fill in end

while True:
    # Establish the connection
    print("Ready to serve...")
    # Fill in start
    connectionSocket, addr = serverSocket.accept()
    # Fill in end
    try:
        # Fill in start
        message = connectionSocket.recv(6789)
        # Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        # Fill in start
        outputdata = f.read()
        # Fill in end
        # Fill in start
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        error_message = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        error_message += (
            "<!doctype html><html><body><h1>404 Not Found<h1></body></html>"
        )
        connectionSocket.send(error_message.encode())
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
