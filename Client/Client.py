import socket

def client_program(idx):
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    if idx == "end":
        client_socket.send(str(idx).encode())
        data = client_socket.recv(1024).decode()
        if data == "Connection is terminated!":
            client_socket.close()  # close the connection
            return "Server closed!"
    else:
        client_socket.send(str(idx).encode())
        receivedString = ""
        while True:
            data = client_socket.recv(1024).decode()
            if data == "done":
                #print("Connection closed!")
                client_socket.close() # close the connection
                break
            receivedString += data

        tmp = receivedString.split(";")
        tmp = tmp[:len(tmp)-1]
        for i, item in enumerate(tmp):
            if item == "None":
                tmp[i] = None
            if item.isdigit():
                tmp[i] = int(item)
        return tuple(tmp)