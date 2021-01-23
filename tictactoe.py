"""TicTacToe. A module for playing a simple game.

Your Name Goes Here

Answer the following questions using your implementation:

1. Is it significantly better to play as 'X', or 'O', or neither?
    It roughly twice as likely to win as 'X' than 'O'.in a standard size game.
    Results: 10000000 trials: 1 wins 0.59, -1 wins 0.29, stalemates 0.13

2. Describe an approach that will allow you to test if all first moves
   are equally good for 'X'. The method should be valid (yields
   correct results) and efficient (use minimal calculation).
    There are only three starting moves that are actually different.
    'X' can start in a corner, the middle, or a side.


3. Using the method described in (2), are all first moves for 'X'
   equally good?  If so, what are the odds that 'X' will win?  If not
   which is the best move for 'X' and how much does it improve the
   odds 'X' will win over the second best move?

    The best move for 'X' is to start in the middle spot.  This provides
    a 69% chance for winning, which is 8% greater than starting in a corner.

    Middle: State is: (0, 0, 0, 0, 1, 0, 0, 0, 0)
    10000000 trials: 1 wins 0.69, -1 wins 0.19, stalemates 0.11

    Corner: State is: (1, 0, 0, 0, 0, 0, 0, 0, 0)
    10000000 trials: 1 wins 0.61, -1 wins 0.26, stalemates 0.13

    Side: State is: (0, 1, 0, 0, 0, 0, 0, 0, 0)
    10000000 trials: 1 wins 0.54, -1 wins 0.34, stalemates 0.13


3. If 'X' moves into the bottom middle square, what is O's best
   response? (i.e.  the response that is *least likely* to yield a win
   for X)?
    The best response is to take the middle spot.

    State is: (0, 0, 0, 0, -1, 0, 0, 1, 0)
    10000000 trials: 1 wins 0.41, -1 wins 0.44, stalemates 0.14

    python3 tictactoe.py --state 000000210 --mc 1000000
    python3 tictactoe.py --state 000002010 --mc 1000000
    python3 tictactoe.py --state 000020010 --mc 1000000
    python3 tictactoe.py --state 002000010 --mc 1000000
    python3 tictactoe.py --state 020000010 --mc 1000000



4. As the board gets bigger, is X's first move more, or less,
   strategically important?

   X's first move becomes much less strategically important.  Increasing the
   board size to 5 X 5 results provides six different unique starting positions.
   The greatest advantage is still by starting in the middle, but it is much
   less significant.  The center position provides a 28% chance, edging out
   the second place by only 2% and the worst performers by only 5%.

    python3 tictactoe.py  -n 5 --state 0000000000000000000000001 --mc 1000000
    python3 tictactoe.py  -n 5 --state 00000 00000 00000 00000 00010 --mc 1000000
    python3 tictactoe.py  -n 5 --state 0000000000000000000000100 --mc 1000000
    python3 tictactoe.py  -n 5 --state 0000000000000000001000000 --mc 1000000
    python3 tictactoe.py  -n 5 --state 00000 00000 00000 00100 00000 --mc 1000000
    python3 tictactoe.py  -n 5 --state 0000000000001000000000000 --mc 1000000

python3 tictactoe.py  -n 7 --state 0000000000000000000000001000000000000000000000000 --mc 1000000


"""
import sys
from random import randrange
import time


def int_input(state, mover):
    print("%s's turn...(0..%d)" % (TicTacToe.Chrs[mover], len(state) - 1))
    return int(input())


class TicTacToe():
    """A Class representing the game of TicTacToe."""
    Column = 0
    Row = 1
    Diagonal = 2
    StaleMate = 3
    # 0 = blank, 1 = X, -1=0
    Chrs = {0: ' ', 1: 'X', -1: 'O'}

    def __init__(self, n=3):
        """Create a n-by-n tic-tac-toe game. n=3 by default"""

        self.n = n
        self.n2 = n**2
        self.reset()

        # set state=none IF nothing passed for state
    def reset(self, state=None):
        """Reset the game to the specified state, or to an empty board.
        A state is encoded as a list (or tuple) of elements in {-1, 0, 1}.
        -1 represents an 'O' (player 2), 0 represents an empty space and
        1 represents an 'X' (player 1).  The state is assumed to have an
        appropriate number of 'X's relative to the number of 'O's."""
        if state:
            ones = sum([1 for i in state if i == 1])
            negs = sum([1 for i in state if i == -1])
            # ones (x's) go first

            # ensure imported state has valid amt of X's and O's
            assert ones == negs or ones == negs + 1, "X's (1's) go first."
            # esnures imported state is correct size
            assert len(state) == self.n2, "the specified state is not the correct length"
            # The game state is kept here as a list of values.
            # 0  indicates the space is unoccupied;
            # 1  indicates the space is occupied by Player 1 (X)
            # -1 indicates the space is occupied by Player 2 (O)

            # list() converts given tuple to a list
            self.board = list(state)
            # returns value from adding all entries in board
            s = sum(state)
            if s == 0:
                self.turn = 1
            else:
                self.turn = -1

        # new board
        else:
            self.board = [0] * (self.n2)
            self.turn = 1

    def move(self, where):
        """_ Part 1: Implement This Method _

        Make the current player's move at the specified location/index and
        change turns to the next player; where is an index into the board in
        the range 0..(n**2-1)

        If the specified index is a valid move, modify the board,
        change turns and return True.

        Return False if the specified index is unopen, or does not exist"""

        # check for possibily valid (within board) and empty spot
        if where > (self.n2 - 1) or self.n < 0 or self.board[where] != 0:
            return False

        self.board[where] = self.turn

        # change turns
        if self.turn == 1:
            self.turn = -1
        else:
            self.turn = 1

        return True

    # pushes board out from left edge
    def leftMargin(self, spacing=5):
        print(" " * spacing, end='')

    def show(self, stream=sys.stdout):
        """_ Part 2: Implement This Method _
        Displays the board on the specified stream."""
        """ idSpot used to identify the square on the board if open,
            offset to left to help with quickly seeing open spots """
        sys.stdout = stream
        for i in range(self.n):
            # first line of row
            self.leftMargin()
            for j in range(self.n):
                print(" " * 3, end='')
                if j < (self.n - 1):
                    print("|", end='')
            print("")

            self.leftMargin()

            # second line of row-- with char
            for j in range(self.n):
                mark = TicTacToe.Chrs[0]
                curSpot = (i * self.n) + j
                idSpot = curSpot
                if self.board[curSpot] == -1:
                    # check for 'O'
                    mark = TicTacToe.Chrs[-1]
                    idSpot = ' '
                elif self.board[curSpot] == 1:
                    # check for 'X'
                    mark = TicTacToe.Chrs[1]
                    idSpot = ' '

                # allow for id on boards larger than n = 9
                if mark == ' ' and idSpot > 9:
                    mark = ''

                print(f"{idSpot}{mark} ", end='')
                if j < (self.n - 1):
                    print("|", end='')
            print("")

            self.leftMargin()

            # 3rd line/ divider
            if i < (self.n - 1):
                for j in range(self.n):
                    print("___", end='')
                    if j < (self.n - 1):
                        print("|", end='')
                print("")

        for j in range(self.n - 1):
            print("   |", end='')
        print("")

    def is_win(self):
        """_ Part 3: Implement This Method _

        Determines if the current board configuration is an end game.
        For a board of size n, a win requires one player to have n tokens
        in a line (vertical, horizontal or diagonal).

        Returns:
         (TicTacToe.Column, c, player): if player wins in column c
         (TicTacToe.Row, r, player): if player wins in row r
         (TicTacToe.Diagonal, 0, player): if player wins via
           a diagonal in the upper-left corner
         (TicTacToe.Diagonal, 1, player): if player wins via a
           diagonal in the upper-right corner
         (TicTacToe.StaleMate, 0, 0): if the game is a stalemate
         False: if the end state is not yet determined
        """
        # column win
        # check start of each col for player char
        boardFull = True # flips if open space found
        player = 1
        wincount = 1

        for i in range(self.n):
            wincount = 1

            if self.board[i] != 0:
                player = self.board[i]
                curSpot = i + self.n
                for j in range(1, self.n):
                    if self.board[curSpot] == player:
                        wincount += 1
                        curSpot += self.n
                    else:
                        if self.board[curSpot] == 0:
                            boardFull = False
                        break
                if wincount == self.n:
                    return (TicTacToe.Column, i, self.board[i])
            else:
                boardFull = False

        # diagonal win
        # check for odd n -- diagonal only possible on odd boards
        if self.n % 2 == 1:
            # check middle spot -- can only win if owned by player
            middlespot = (self.n * (self.n // 2) + (self.n // 2))

            if self.board[middlespot] != 0:
                curSpot = 0
                wincount = 0

                for i in range(self.n):
                    if self.board[curSpot] == self.board[middlespot]:
                        wincount += 1
                        curSpot += (self.n + 1)
                    else:
                        break
                if wincount == self.n:
                    return (TicTacToe.Diagonal, 0, self.board[middlespot])

                # check for win from top right
                curSpot = (self.n - 1)
                wincount = 0

                for i in range(self.n):
                    if self.board[curSpot] == self.board[middlespot]:
                        wincount += 1
                        curSpot += (self.n - 1)
                    else:
                        break
                if wincount == self.n:
                    return (TicTacToe.Diagonal, 1, self.board[middlespot])
            else:
                boardFull = False


        # row win check and full check for open spaces
        for i in range(0, self.n2, self.n):
            wincount = 1
            player = self.board[i]
            if self.board[i] != 0:
                for j in range(i + 1, i + self.n):
                    if self.board[j] == player:
                        wincount += 1
                    else:
                        if not boardFull:
                            break
                        elif self.board[j] == 0:
                            boardFull = False
                            break
            else:
                boardFull = False

            if wincount == self.n:
                return (TicTacToe.Row, i // self.n, self.board[i])

        if boardFull:
            return (TicTacToe.StaleMate, 0, 0)
        else:
            return False

    def describe_win(self, win):
        """Provides a text representation of an end-game state."""
        reason = {TicTacToe.Row: "Row", TicTacToe.Column: "Column",
                  TicTacToe.Diagonal: "Diagonal"}

        if win[0] == TicTacToe.StaleMate:
            return "StaleMate!"
        if win[0] == TicTacToe.Diagonal:
            if win[1] == 0:
                where = "Upper Left"
            else:
                where = "Upper Right"
        else:
            where = "%d" % win[1]
        return "%s (%d) wins @ %s %s" % (TicTacToe.Chrs[win[2]], win[2],
                                         reason[win[0]], where)

    # def play(self, movefn=int_input, outstream=None, showwin=True):
    def play(self, movefn=int_input, outstream=None, showwin=True):
        """_ Part 4: Implement This Method _


        Play the game of tictactoe!

        Arguments:
        movefn - a function that will provide possibly valid moves.
        outstream - a stream on which to show the game (if provided)
        showwin - if True, explicitly indicate the game is over
                  and describe the win

        Play should work (roughly) as follows:
         - verify the game is not in an end state
         - if outstream is provided, display the game state (using show())
         - acquire the next move from the movefn (see note below).
         - repeat steps above

         when an end state is reached:
         - print the state (if outstream is defined) and
         - print 'Game Over!' along with a description of the win
           if showwin is True.

        the movefn should take two arguments:
          (1) the game state; and (2) the current player
        """

        checkWin = self.is_win()

        while not checkWin:
            if outstream:
                self.show()

            # get state
            theState = self.get_state()

            theMove = movefn(theState, self.turn)

            validMove = self.move(theMove)

            while not validMove:
                theMove = movefn(theState, self.turn)
                validMove = self.move(theMove)

            checkWin = self.is_win()



        if checkWin:
            print(self.describe_win(checkWin))


    def get_state(self):
        """Get the state of the board as an immutable tuple"""
        return tuple(self.board)


def mc(state, n, debug=False):
    """_ Part 5: Implement This Method _

    Run a monte-carlo experiment in which we play the game using random
    moves.  Start each game at the specified state and run n
    simulations. Record the distribution of outcomes. Monte-carlo
    experiments such as this are used to evaluate states in complex
    games such as chess and go.

    Return a 4-tuple of:
    (games played, % won by player-1, % won by player-2, % stalemates)

    """
    games = 0
    xWin = 0
    oWin = 0
    stale = 0
    t = TicTacToe(args.n)

    # create list of available move remaining from state
    availMoves = []
    for i in range(len(state)):
        if state[i] == 0:
            availMoves.append(i)

    for i in range(n):
        t.reset(state)
        checkWin = t.is_win()
        rmngMoves = availMoves.copy()

        while not checkWin:
            # get random move from valid move list
            theMove = rmngMoves.pop(randrange(len(rmngMoves)))
            t.move(theMove)

            checkWin = t.is_win()

        if checkWin:
            games += 1
            if checkWin[2] == 1:
                xWin += 1
            elif checkWin[2] == -1:
                oWin += 1
            else:
                stale += 1
    return (games, xWin / games, oWin / games, stale / games)


if __name__ == "__main__":
    import argparse
    import random
    parser = argparse.ArgumentParser()
    parser.add_argument("--play", action='store_true')
    parser.add_argument("--state",
                        help="initial state comprised of values in {0,1,2}")
    parser.add_argument("--mc", type=int, default=1000,
                        help="monte carlo trials; default=%(default)s")
    parser.add_argument("-n", type=int, default=3,
                        help="board length,width; default=%(default)s")
    args = parser.parse_args()

    if args.state:
        # At the command line state will come in as a string drawn
        # from {0,1,2}.  -1 is not used here since it's awkwardly
        # two characters.
        assert len(args.state) == args.n**2, \
            "Expected string with %d elements" % (args.n**2)

        # state is input from set {0,1,2} but needs to be translated into
        # {0,1,-1} by changing '2' entries to -1.
        state = [int(z) for z in args.state]
        stateset = set(state)
        assert stateset.issubset(set([0, 1, 2])), \
            "Expected string with elements 0,1,2"
        state = [-1 if s == 2 else s for s in state]
        state = tuple(state)
        print("State is:", state)
    else:
        state = tuple([0]*(args.n**2))

    t = TicTacToe(args.n)
    if args.play:
        t.reset(state)
        t.play(outstream=sys.stdout)

    elif args.mc:
        start = time.time()
        (games, one, two, stale) = mc(state, args.mc)
        end = time.time()
        delta = end - start
        print(f"{delta} seconds elapsed")
        print("%d trials: 1 wins %.2f, "
              "-1 wins %.2f, stalemates %.2f" % (games, one, two, stale))
