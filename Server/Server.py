import socket
import Server.DataBase as DB
import time


def server_program():
    print("Start Data Base setup.")
    DB.startDB()
    print("Data Base is up to date.")
    print("")
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    print("Server ready to listen!")
    # configure how many client the server can listen simultaneously
    while True:
        server_socket.listen(2)
        conn, address = server_socket.accept()  # accept new connection

        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        #print("Data received: " + data)
        if data == "end":
            conn.send("Connection is terminated!".encode())
            conn.close()  # close the connection
            break

        data = DB.readDBOut(int(data))
        #print(data)
        for d in data:
            conn.send((str(d)+";").encode())  # send data to the client
        conn.send("done".encode())
        #print("Data send!")
    print("Server closed!")
