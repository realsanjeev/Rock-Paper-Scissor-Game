import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostname()
        self.port = 1222
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)
        
    def getid(self):
        return self.id

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except socket.error as e:
            print('Searching connection......!', e)
            
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv((2048)))
        except socket.error as e:
            print(e)
            pass
