from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(
            bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        # print("addresses: ", addresses)
        HANDLE_THREAD = Thread(target=handle_client, args=(client,))
        HANDLE_THREAD.start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clientsNames[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clientsNames[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    # for cl in clients.values():
    # print("All connected clients: ",  cl)

    print("All connected clients: ",  clientsNames.values())
    for sock in clientsNames:
        print("sock: ", sock)
        sock.send(bytes(prefix, "utf8") + msg)
clientsNames = {}
addresses = {}
HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    """We join() ACCEPT_THREAD so that the main script waits for it to complete
     and doesn�t jump to the next line, which closes the server."""
    ACCEPT_THREAD.join()
    SERVER.close()