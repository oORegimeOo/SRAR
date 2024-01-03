import socket

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input
    client_socket.send(message.encode())

    receivedString = ""
    while True:
        data = client_socket.recv(1024).decode()
        if data == "done":
            print("Connection closed!")
            client_socket.close() # close the connection
            break
        if data == "Connection is terminated!":
            print("Server down!")
            client_socket.close()  # close the connection
            break
        receivedString += data

    tmp = receivedString.split(";")
    tmp = tmp[:len(tmp)-1]
    for i, item in enumerate(tmp):
        if item == "None":
            tmp[i] = None
        if item.isdigit():
            tmp[i] = int(item)

    print(tuple(tmp))


if __name__ == '__main__':
    client_program()