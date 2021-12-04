class BingoBoard:
    def parseBoard(self, boardLines):
        self.uncalled_board = []
        for boardStr in boardLines:
            self.uncalled_board.append([int(i) for i in boardStr.split()])
        self.called_board = [[-1]*5 for _ in range(5)] #-1 will indicate empty in either board
        self.has_won = False
        # 90% of the way through I realized I didn't need a "called board", I could have just marked them -1 in the
        # board since you never need the values of the called numbers. Doh!

    def isWinner(self, called):
        # if we've already won, don't consider
        if self.has_won == True:
            return -1
        # if it exists, move drawn number from uncalled to called
        found = None
        for coln, rowl in enumerate(self.uncalled_board):
            if called in rowl:
                found = (coln, rowl.index(called))
        if found != None:
            self.uncalled_board[found[0]][found[1]] = -1
            self.called_board[found[0]][found[1]] = called
        else:
            return -1;
        # check rows
        for row in self.called_board:
            if not -1 in row:
                return self.sumUncalled()

        # check columns
        for i in range(len(self.called_board[0])):
            sum = 0
            for row in self.called_board:
                if row[i] != -1:
                    sum += row[i]
                else:
                    sum = -1
                    break
            if sum != -1:
                return self.sumUncalled()
            
        # if winner, return sum of unmarked numbers, otherwise return -1
        return -1
    
    def sumUncalled(self):
        # we have a winner so mark us won to remove further consideration
        self.has_won = True
        sum = 0
        for row in self.uncalled_board:
            for num in row:
                if num != -1:
                    sum += num
        return sum

    def printBoard(self):
        print("Uncalled")
        print(self.uncalled_board)
        print("Called")
        print(self.called_board)

    

def bingo() -> None:
    with open('input.txt') as f:
        lines = f.read().splitlines()
        #load the called line and remove the line to make board parsing easier
        called = [int(i) for i in lines[0].split(',')]
        del lines[0:1]
        
        #load up the boards
        boards = []
        for boardIndex in range(0, len(lines), 6):
            newBoard = BingoBoard()
            boards.append(newBoard)
            newBoard.parseBoard(lines[boardIndex+1:boardIndex+6])  #+1 skips the blank line between boards

        # check the boards, this could be done on parse I guess but this feels better, going through the called once
        for calledN in called:
            for i, board in enumerate(boards):
                sum = board.isWinner(calledN)
                if sum != -1:
                    print("Bingo! Answer", sum * calledN, "Called#", calledN, "Board#", i)

if __name__ == '__main__':
    bingo()