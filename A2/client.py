from socket import *
import sys

serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]

hostPort = "%s:%d" % (serverHost, serverPort)
try:
    print(serverHost)
    print(serverPort)
    print(filename)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverHost, serverPort))
    header = "GET /%s HTTP/1.1\r\nHost: %s\r\n\r\n" % (filename, hostPort)
    print(header)
    clientSocket.send(header.encode())
except IOError:
    print("Error: Connection failed")
    sys.exit(1)

response = clientSocket.recv(1024)
output = []
while response:
    output.append(response.decode())
    response = clientSocket.recv(1024)

clientSocket.close()
print("".join([str(elem) for elem in output]))
