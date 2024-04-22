import socket
import threading
port = 8080
ip= socket.gethostbyname(socket.gethostname())
size=10
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ip,port))

def handleClient(conn,addr):
    print(f"[{addr}] connected!")
    userMsg=""
    while True:
        msg=conn.recv(size).decode()
        if(len(msg)>0):
            trimmedMsg=msg.split('\\0')[0]
            if(trimmedMsg=="01010101"):
                print(f"[{addr}]:{userMsg}")
                userMsg=""
            else:
                userMsg=userMsg+trimmedMsg
            if(trimmedMsg=="Disconnect"):
                break
    print(f"[{addr}]: closed")
    conn.close()

def start():
    print("[Server Started]")
    server.listen()
    print("[Server Listening]")
    while True:
        conn,addr= server.accept()
        thread=threading.Thread(target=handleClient,args=[conn,addr])
        thread.start()

start()
