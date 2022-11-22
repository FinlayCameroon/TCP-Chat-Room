import threading
import socket

host = '127.0.0.1'
port = 19584

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
usernames = []

def sendMessage(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            sendMessage(message)
        except:
            index = clients.index()
            clients.remove(client)
            username = usernames[index]
            sendMessage(f"{username} left the chat".encode("ascii"))
            usernames.remove(username)
            break


def receiveMessages():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        client.send('USERNAME'.encode("ascii"))
        username = client.recv(1024).decode("ascii")
        usernames.append(username)
        clients.append(client)
        print(f"Username of the client is {username}")
        sendMessage(f"{username} has joined the chat".encode("ascii"))
        client.send("Connected to the server".encode("ascii"))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is Live...")
receiveMessages()