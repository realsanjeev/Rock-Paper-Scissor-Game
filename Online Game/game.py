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
        if self.moves[0] is None or self.moves[1] is None:
            return -1 # No winner if moves aren't set
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        if p1 == p2:
            return 2 # Tie game

        winner = -1
        if (p1 == 'R' and p2 == 'S') or \
             (p1 == 'P' and p2 =='R') or \
             (p1 == 'S' and p2 == 'P'):
            return 0 # p1 win
        else:
            return 1 # p2 win


    def reset_action(self):
        '''
        reset game after one player win
        '''
        self.p1_action = False
        self.p2_action = False
        self.moves = [None, None]
