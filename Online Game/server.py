'''
Server connection for multi player online
'''
import pickle
import socket
from _thread import start_new_thread
from game import Game

serverAddr = socket.gethostname()
print('#'*10, serverAddr)
PORT = 1222
connected = set()
games = {}
ID_COUNT = 0

connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(connect)

try:
    connect.bind((serverAddr, PORT))
except socket.error as er:
    print('#'*10, 'error')
    print(er)

connect.listen(2)
print('Wating for connection, Server started')

def threading_client_connection(connection, player, id_game):
    '''
    Args:
        connection: connection with network
        id_game: id for game between two game
    '''
    global ID_COUNT
    connection.send(str.encode(str(player)))

    while True:
        try:
            data = connection.recv(4096).decode()
            if id_game in games:
                game = games[id_game]

                if not data:
                    break
                else:
                    if data == 'reset':
                        game.reset_action()
                    elif data != 'get':
                        game.play(player, data)
                connection.sendall(pickle.dumps(game))
            else:
                break
        except socket.error:
            break
    print('Lost Connection')
    try:
        del games[id_game]
        print('closing Game', id_game)
    except socket.error as err:
        print(f'Error while deleting game_id: {err}')
    ID_COUNT -= 1
    connection.close()


while True:
    conn, addr = connect.accept()
    print('Connected to: ', addr)

    ID_COUNT += 1
    PLAYER = 0
    GAME_ID = (ID_COUNT - 1)//2  # return integer
    if ID_COUNT % 2 == 1:
        games[GAME_ID] = Game(GAME_ID)
        print('creating a new game...')
    else:
        games[GAME_ID].ready = True
        PLAYER = 1
    start_new_thread(threading_client_connection, (conn, PLAYER, GAME_ID))
