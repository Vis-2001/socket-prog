import socket

port = 8080
ip= socket.gethostbyname(socket.gethostname())
size=10
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
endofmsg= "01010101\\0".encode('utf-8')
client.connect((ip,port))

def sendMsg(msg):
    ind=0
    while ind+size<len(msg):
        minimsg=msg[ind:ind+size-3]+'\\0'
        minimsg=minimsg.encode('utf-8')+b'0'*(size-len(minimsg))
        client.send(minimsg)
        ind=ind+size-3
    if(ind!=len(msg)-1):
        minimsg=msg[ind:]+'\\0'
        minimsg=minimsg.encode('utf-8')+b'0'*(size-len(minimsg))
        client.send(minimsg)
    client.send(endofmsg)
    

msg="Enter msg"
while msg!="Disconnect":
    msg=input("Enter Message to send to the server:")
    sendMsg(msg)
