'''Created for main.py'''
class Game:
    '''Class for game event processing'''

    def __init__(self, id):
        '''
        Args:
            id: id of game
        '''
        self.p1_action = False
        self.p2_action = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0

    def get_player_move(self, player):
        '''
        Args:
            player -> player eho made move
        Retuen:
            Move of player
        '''
        return self.moves[player]

    def play(self, player, move):
        '''
        Args:
            player: id of player
            move: which option id delected by user
        '''
        self.moves[player] = move
        if player == 0:
            self.p1_action = True
        else:
            self.p2_action = True

    def connection(self):
        '''
        Connect game to server to another player
        '''
        return self.ready

    def action(self):
        '''
        Return action of player1 and player2
        '''
        return self.p1_action and self.p2_action

    def winner(self):
        '''
        return winner of game
        '''
        p1_player = self.moves[0].upper()[0]
        p2_player = self.moves[1].upper()[0]

        winner = -1
        if (p1_player == 'R' and p2_player == 'S') or\
             (p1_player == 'P' and p2_player =='R') or\
             (p1_player == 'S' and p2_player == 'P'):
            winner = 0
        elif (p2_player == 'R' and p1_player == 'S') or\
             (p2_player == 'P' and p1_player =='R') or\
             (p2_player == 'S' and p1_player == 'P'):
            winner = 1
        return winner


    def reset_action(self):
        '''
        reset game after one player win
        '''
        self.p1_action = False
        self.p2_action = False
