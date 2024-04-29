import socket
from socket import gethostbyname, gethostname
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

class MySocket:

    def __init__(self,myIp,OutIP, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.Ip=myIp
        self.oIP=OutIP
        self.conectS=True

    
    def send(self,mensage):
        if self.conectS:    
            self.initClient()
        self.tube.send(mensage)
     
    def initClient(self):
        self.sock.connect((self.oIP, 12345))
        self.conectS=False
        self.tube=self.sock   
         
    def initServer(self):  
        self.sock.bind((self.Ip,12345))
        self.conectS=False
        self.sock.listen(1)
        conn, address = self.sock.accept()
        self.tube=conn
        
    def receive(self):
        if(self.conectS):
            self.initServer()
        while True:
            dat=self.tube.recv(1024)
            if dat:
                break
        
        return dat 

    def closeConect(self):
        self.sock.close()
        self.conectS=True
def getIpPublic():
    return gethostbyname(gethostname()) 

    