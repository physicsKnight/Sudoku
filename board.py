import config as cf
import random
import time

class Board():
    def __init__(self):
        self.window = None
        self.solvingData = [0, False]
        self.grid = [[{0: True} for i in range(9)] for i in range(9)]

    def reset(self):
        for i in range(9):
            for j in range(9):
                self.grid[i][j] = {0: True}
        cf.selected = None
        self.solvingData = [0, False]

    def generatePuzzle(self):
        self.reset()
        for i in range(20):
            while True: # find a valid num
                col = random.randrange(9)
                row = random.randrange(9)
                num = random.randrange(1, 10)
                # if a free cell is found and the number is valid
                if self.getNum(col, row) == 0 and self.isValid(col, row, num):
                    break
            # we place the number directly so that we can lock it
            self.grid[col][row] = {num: False}

            if i >= 17: # minimum of 17 clues
                grid = [col[:] for col in self.grid]
                if self.solve():
                    self.grid = grid
                    return True
                self.solvingData = [0, False]
        return False

    def placeNum(self, col, row, num):
        # check value of cell in case it is locked
        if list(self.grid[col][row].values())[0]:
            self.grid[col][row] = {num: True}

    def getNum(self, col, row):
        return list(self.grid[col][row])[0]

    def solve(self):
        # if we've made over 100 attempts then the board is probably not solvable
        # therefore we exit the call stack and generate a new board instead
        if (self.solvingData[0] > 100):
            self.solvingData[1] = True
        if (self.solvingData[1]):
            return False

        pos = self.findNextCell()
        if pos == None: return True # base case
        for num in range(1, 10):
            if self.isValid(pos[0], pos[1], num):
                self.placeNum(pos[0], pos[1], num)
                if self.solve():
                    return True
                self.placeNum(pos[0], pos[1], 0) # solution didn't work so we reset cell to 0 (backtracking)
        self.solvingData[0] += 1
        return False

    def checkBoard(self):
        # check rows and columns
        for i in range(9):
            colSum = 0
            rowSum = 0
            for j in range(9):
                colSum += self.getNum(i, j)
                rowSum += self.getNum(j, i)
            if rowSum != 45 and colSum != 45:
                return False

        #check sub-grids
        boxSum = 0
        for colOffset in range(0, 9, 3):
            for rowOffset in range(0, 9, 3):
                #iterate through all 9 cells in each sub grid
                for col in range(3):
                    for row in range(3):
                        currCol = col + colOffset
                        currRow = row + rowOffset
                        boxSum += self.getNum(col, row)
                if boxSum != 45:
                    return False
                boxSum = 0
        return True

    def findNextCell(self):
        for col in range(9):
            for row in range(9):
                if (self.getNum(col, row) == 0):
                    pos = (col, row)
                    cf.selected = pos
                    return pos
        return None # No free cell was found, the board is complete

    def isValid(self, col, row, num):
        # the offset moves each posiiton relative to the top left of each sub grid
        rowOffset = row - row % 3
        colOffset = col - col % 3
        return (not self.isPresentRow(col, row, num) and
                not self.isPresentCol(col, row, num) and
                not self.isPresentBox((col, row), rowOffset, colOffset, num))

    def isPresentRow(self, col, row, num):
        for i in range(9):
            if (self.getNum(i, row) == num and i != col):
                return True
        return False

    def isPresentCol(self, col, row, num):
        for j in range(9):
            if (self.getNum(col, j) == num and j != row):
                return True
        return False

    def isPresentBox(self, pos, rowOffset, colOffset, num):
        for col in range(3):
            for row in range(3):
                currCol = col + colOffset
                currRow = row + rowOffset
                if (self.getNum(currCol, currRow) == num and
                   (currCol, currRow) != pos):
                    return True
        return False
