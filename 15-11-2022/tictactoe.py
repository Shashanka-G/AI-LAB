import random

class TicTacToe:
    def __init__(self):
        self.board = [[None for i in range(3)] for j in range(3)]
        mark1 = 'X'
        mark2 = 'O'
        
    def init_board(self):
        tile=0
        for i in range(3):
            for j in range(3):
                self.board[i][j]=tile
                tile+=1
                
    def isEmpty(self,tile):
        i=tile//3
        j=int(tile%3)
        return self.board[i][j]!='X' and self.board[i]!='O'
    
    def player_move(self,tile,mark):
        i = tile//3
        j = int(tile%3)
        self.board[i][j]=mark
        
    def check_if_win(self,last_move=None):
        if last_move is None:
            return False
        i=last_move//3
        j=int(last_move%3)
        return self.check_row(i,j) or self.check_column(i,j) or self.check_major_diag() or self.check_minor_diag()
    
    def check_row(self,x,y):
        mark = self.board[x][y]
        for j in range(3):
            if self.board[x][j]!=mark:
                return False
            
        return True
    
    def check_column(self,x,y):
        mark = self.board[x][y]
        for j in range(3):
            if self.board[j][y]!=mark:
                return False
        return True
    
    def check_minor_diag(self):
        mark = self.board[1][1]
        for i,j in zip(range(3),range(2,-1,-1)):
            if self.board[i][j]!=mark:
                return False
        return True
    
    def check_major_diag(self):
        mark = self.board[1][1]
        for i in range(3):
            if self.board[i][i]!=mark:
                return False
        return True
    
    def ai_move(self,mark):
        if self.isEmpty(4):
            self.player_move(4,mark)
        
        corner_tiles=[0,8,2,5]
        for tile in corner_tiles:
            if self.isEmpty(tile):
                self.player_move(tile,mark)
                return tile
        
        other_tiles = [1,3,7,5]
        for tile in other_tiles:
            if self.isEmpty(tile):
                self.player_move(tile,mark)
                return tile
    
    def multiplayer(self):
        print("Player1:X\n")
        print("Player2:O")
        player = None
        num_moves = 0
        while num_moves<9:
            self.printboard()
            if num_moves%2==0:
                move = int(input("Input tile number, Player1:"))
                player='1'
                self.player_move(move,'X')
            else:
                player='2'
                move = int(input("Input tile number, Player2:"))
                self.player_move(move,'O')
            
            if self.check_if_win(move):
                self.printboard()
                print("Winner is "+player)
                return
            num_moves+=1
        print("It's Draw")
        
    def printborad(self):
        for i in range(3):
            print(self.board[i])
    
    def singleplayer(self):
        playermark = input("Enter your mark:O or X:")
        ai_mark = 'X' if playermark!='X' else 'O'
        toss = random.random()
        flag = True if toss<0.5 else False
        turn = 0
        if flag:
            print("AI starts")
        else:
            print("Player starts")
            
        while turn<9:
            print("Board:\n")
            self.printborad()
            if flag:
                print("AI Move")
                tile = self.ai_move(ai_mark)
            else:
                print("Player move")
                tile = int(input("Enter your move:"))
                self.player_move(tile,playermark)
                if self.check_if_win(tile):
                    self.printborad()
                    if flag:
                        print("AI wins")
                    else:
                        print("Player wins")
                    return
            flag = False if flag else True
            turn+=1
            self.printborad()
        print("Its draw")
        
        
myboard = TicTacToe()
myboard.init_board()
myboard.singleplayer()