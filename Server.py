import socket
import threading

class Server:
    def __init__(self,ip_address,port_no):
        self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((ip_address,port_no))
        self.server.listen()
        print(f"[SERVER] server connected to {ip_address}:{port_no}")
        self.header=64
        self.format="utf-8"
        self.clients={}
        self.disconnect="!DISCONNECT"
    

def main():
    ip_address=socket.gethostbyname(socket.gethostname)
    port=5050
    chat_server=Server(ip_address,port)
    chat_server.run()

if __name__=="__main__":
    main()    