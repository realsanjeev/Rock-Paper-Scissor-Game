'''Program for declaring network connection for multiple game'''
import socket
import pickle

class Network:
    '''
    Network class
    Methods:
        getid() -> get id of client
        connect() -> connect client to network
        send(data) -> transfer data in network
    '''
    def __init__(self):
        '''
        Initiate class for network connection
        '''
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostname()
        self.port = 1222
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def getid(self):
        '''
        Return: getid of client
        '''
        return self.id

    def connect(self):
        '''
        Connect client to server
        '''
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except socket.error as err:
            print('Searching connection......!', err)

    def send(self, data):
        '''
        Args:
            data: pickle_format
        Return:
            load the data from pickle format
        '''
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv((2048)))
        except socket.error as err:
            print(err)
