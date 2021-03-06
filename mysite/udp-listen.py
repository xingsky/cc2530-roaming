import socket, sys

class MiniServer:
    h = ''
    p = ''
    m = ''
    def __init__(self, host, port):
        self.h = host
        self.p = int(port)
        #self.m = mode
        
    def serverT4(self):
        tcpT4Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "Server Socket Created......."
        tcpT4Server.bind((self.h, self.p))
        print "Wating for connecting......."
        tcpT4Server.listen(5)
        while True:
            clientSock, clientaddr = tcpT4Server.accept()
            print "Connected from: ", clientSock.getpeername() 
            clientSock.send('Congratulations........')
            while True:
                buf = clientSock.recv(1024)
                print buf
            #clientSock.close()
    
    def udpT4(self):
        udpT4Server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print "UDP TCP IPv4 Mode Start....."
        udpT4Server.bind((self.h, self.p))
        print "UDP Server Start"
        while True:
            udpT4Data, udpT4ServerInfo = udpT4Server.recvfrom(1024)
            print "Receive from ", udpT4ServerInfo, " and The Data send from The Client is :", udpT4Data

    def serverT6(self):
        tcpT6Server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        print "Server Socket Created......."
        tcpT6Server.bind((self.h, self.p))
        print "Wating for connecting......."
        tcpT6Server.listen(5)
        while True:
            clientSock, clientaddr = tcpT6Server.accept()
            print "Connected from: ", clientSock.getpeername() 
            clientSock.send('Congratulations........')
            #clientSock.close()
						
    def udpT6(self):
        udpT6Server = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        print "UDP TCP IPv6 Mode Start....."
        udpT6Server.bind((self.h, self.p))
        print "UDP Server Start"
        while True:
            udpT4Data, udpT6ServerInfo = udpT6Server.recvfrom(1024)
            print  udpT4Data

if __name__ == "__main__":
    x = MiniServer('bbbb::212:4b00:205:f000', 5678)
    x.udpT6()