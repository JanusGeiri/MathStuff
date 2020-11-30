class TicTacToe:
    def __init__(self, inp_board=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
        self.board = inp_board

    def getDiag(self):
        board = self.board
        diag1 = []
        diag2 = []
        for i in range(3):
            for j in range(3):
                diag1.append(board[i][j])
                diag2.append(board[2-i][j])
        return [diag1, diag2]

    def getCols(self):
        return [[self.board[i][j] for i in range(3)] for j in range(3)]

    def wincheck_1(self):
        for row in self.board:
            if sum(row) == 3:
                return True
        for diag in self.getDiag():
            if sum(diag) == 3:
                return True
        for col in self.getCols():
            if sum(col) == 3:
                return True
        return False

    def wincheck_2(self):
        for row in self.board:
            if sum(row) == -3:
                return True
        for diag in self.getDiag():
            if sum(diag) == -3:
                return True
        for col in self.getCols():
            if sum(col) == -3:
                return True
        return False

    def printBoard(self):
        dummy_board = self.board
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 1:
                    dummy_board[i][j] = 'X'
                elif self.board[i][j] == -1:
                    dummy_board[i][j] = 'O'
                elif self.board[i][j] == 0:
                    dummy_board[i][j] = '-'
        for row in dummy_board:
            print('|', end='')
            for item in row:
                print(item+'|', end='')
            print('')

    def play(self):
        print('Game Started')


board = TicTacToe([[1, 0, 1], [-1, 0, -1], [0, 0, 0]])

board.printBoard()
board.play()
