
import itertools


class board:

    def __init__(self, input):
        self._board = {}
        self._row =  [0] * 5 
        self._column = [0] * 5
        self._marked = [0] * 25
        self._complete_line = [False] * 10
        self._complete = False
        self._marked_sum = 0 
        self.make_board(input)

    # should have used numpy
    def make_board(self,input):
        for i in range(0,5):
            for j in range(0,5):
                self._board[input[(5*i) + j]] = (i,j)
    
    def in_board(self,number):

        try:
            x,y = self._board[number]
            self._row[x] +=1
            if self._row[x] == 5:
                self._complete_line[x] = True
                self._complete = True 
            self._column[y] +=1
            if self._column[y] == 5:
                self._complete_line[5+y] = True
                self._complete = True 
            self._marked_sum += number
            return True

        except KeyError:
            return False    

    #this can be a getter.
    def win(self):
        return self._complete

    def unmarked_score(self):
        total = 0
        for key in self._board.keys():
            total +=key
        return total-self._marked_sum

    def reset(self):
        self._row =  [0] * 5 
        self._column = [0] * 5
        self._marked = [0] * 25
        self._complete_line = [False] * 10
        self._complete = False
        self._marked_sum = 0
        return self



def reader(filename):

    draws = 0
    boards = []
    with open(filename,"r") as file:
        data = [line.strip() for line in file]
        draws = [int(x) for x in data[0].split(",")]

        for idx in range(2,len(data),6):
            to_int = lambda x: [int(x) for x in data[x].split()]

            boards.append(list(itertools.chain(to_int(idx), to_int(idx+1), to_int(idx+2), to_int(idx+3), to_int(idx+4))))

        return draws,boards
    

# part a 

draws,board_sets = reader("4_input.txt")

board_obj = [board(x) for x in board_sets]

win_board = None
win_num = -1
for num in draws:
    for tile in board_obj:
        if tile.in_board(num):
            if tile.win():
                win_board = tile
                win_num = num
                break

    if win_num != -1:
        break

print(win_num*win_board.unmarked_score())


#part b 
f = lambda x: x.reset()
board_obj = [f(tile) for tile in board_obj]

last_win_board = None
last_win_num = -1 
for num in draws:
    for idx,tile in enumerate(board_obj):

        # if board has already been completed skip
        if tile.win():
            continue
        if tile.in_board(num):
            if tile.win():
                last_win_board = tile
                last_win_num = num

print(last_win_num*last_win_board.unmarked_score())
