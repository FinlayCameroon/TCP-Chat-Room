import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',19584))


username = input("Choose a nickname: ")


def receiveMessages():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "USERNAME":
                client.send(username.encode("ascii"))
            else:
                print(message)
        except:
            print("An error occurred")
            client.close()
            break


def write():
    while True:
        message = f"{username}: {input('')}"
        client.send(message.encode("ascii"))



receiveThread = threading.Thread(target=receiveMessages)
writeThread = threading.Thread(target=write)

try:
    receiveThread.start()
    writeThread.start()
except:
    print("error")
