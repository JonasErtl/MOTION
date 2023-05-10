import socket
import threading

HEADER = 64
PORT = 5050 
#SERVER = socket.gethostbyname(socket.gethostname()) For some reason this returns 127.0.0.1 on my computer 
SERVER = "192.168.178.29" #Hardcoded ip address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#file1 = open("file.txt", "w")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handleClient(conn, addr):
    print(f"[NEW CONNECTION {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode()
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            file1 = open("file.txt", "w")
            file1.write(msg)
            #file1.flush()
            file1.close()
            print(f"[{addr}] {msg}")
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True: 
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] The server is starting...")
start()
