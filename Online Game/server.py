import pickle
from _thread import *
import socket
from game import Game

serverAddr = socket.gethostname()
print('#'*10, serverAddr)
port = 1222

connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(connect)

try:
    connect.bind((serverAddr, port))
except socket.error as er:
    print('#'*10, 'error')
    print(er)

connect.listen(2)
print('Wating for connection, Server started')

connected = set()
games = {}
idCount = 0

def threading_client_connection(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == 'reset':
                        game.resetAction()
                    elif data != 'get':
                        game.play(p, data)
                conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break
    print('Lost Connection')
    try:
        del games[gameId]
        print('closing Game', gameId)
    except:
        pass
    idCount -= 1
    conn.close()


while True:
    conn, addr = connect.accept()
    print('Connected to: ', addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2  # return integer
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print('creating a new game...')
    else:
        games[gameId].ready = True
        p = 1
    start_new_thread(threading_client_connection, (conn, p, gameId))