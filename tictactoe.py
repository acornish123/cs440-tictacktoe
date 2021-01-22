"""TicTacToe. A module for playing a simple game.

Your Name Goes Here

Answer the following questions using your implementation:

1. Is it significantly better to play as 'X', or 'O', or neither?

2. Describe an approach that will allow you to test if all first moves
   are equally good for 'X'. The method should be valid (yields
   correct results) and efficient (use minimal calculation).

3. Using the method described in (2), are all first moves for 'X'
   equally good?  If so, what are the odds that 'X' will win?  If not
   which is the best move for 'X' and how much does it improve the
   odds 'X' will win over the second best move?

3. If 'X' moves into the bottom middle square, what is O's best
   response? (i.e.  the response that is *least likely* to yield a win
   for X)?

4. As the board gets bigger, is X's first move more, or less,
   strategically important?

"""
import sys


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
        print("reset")
        if state:
            ones = sum([i for i in state if i == 1])
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

        # check for possibily valid
        if where > (n2 - 1) or n < 0:
            return False

        # check board position is empty
        if self.board[where] != 0:
            return False

        self.board[where] = self.turn

    def leftMargin(self, spacing=5):
        print(" " * int(spacing), end='')




    def show(self, stream=sys.stdout):
        """_ Part 2: Implement This Method _

        Displays the board on the specified stream."""
        # x = 'X'
        sys.stdout = stream
        print("show")
        for i in range(self.n):
            # first line of row
            self.leftMargin()
            for j in range(self.n):
                print(" " * 3, end='')
                if j < (self.n - 1):
                    print("|", end='')
            print("")

            # second line of row-- with char
            self.leftMargin()

            for j in range(self.n):
                mark = ' '
                if self.board[(i * self.n) + j] == -1:
                    mark = 'O'
                    # mark = (i * self.n) + j
                elif self.board[(i * self.n) + j] == 1:
                    mark = 'X'
                    # mark = (i * self.n) + j

                print(f" {mark} ", end='')
                # print(f" {self.board[i]} ", end='')
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
        boardFull = 0

        for i in range(self.n - 1):
            wincount = 0
            if self.board[i] == self.turn:
                wincount += 1
                # check for win
                for j in range(1, self.n - 1):
                    if self.board[i + (self.n * j)] == self.turn:
                        wincount += 1
                    else:
                        break
                if wincount == self.n:
                    print("col win")
                    return (TicTacToe.Column, i, self.turn)

        # diagonal win
        # check for odd n -- diagonal only possible on odd boards
        if self.n % 2 == 1:
            # check middle spot -- can only win if owned by player
            middlespot = (self.n * (self.n // 2) + (self.n // 2))
            if self.turn == self.board[middlespot]:
                curspot = 0
                wincount = 0
                # now check for a win
                for i in range(self.n):
                    if curspot == self.turn:
                        wincount += 1
                        curspot += (self.n + 1)
                    else:
                        break
                if wincount == self.n:
                    print("X win")

                    return (TicTacToe.Diagonal, 0, self.turn)

                curspot = (self.n - 1)
                wincount = 0
                for i in range(self.n):
                    if curspot == self.turn:
                        wincount += 1
                        curspot += (self.n - 1)
                    else:
                        break
                if wincount == self.n:
                    print("X2 win")

                    return (TicTacToe.Diagonal, 1, self.turn)

        # row win
        for i in range(self.n - 1, self.n2 - self.n, self.n):
            wincount = 0
            if self.board[i] == self.turn:
                wincount += 1
                for j in range(i + 1, i + self.n):
                    print(j)
                    if self.board[j] == self.turn:
                        wincount += 1
                    elif self.board[j] == 0:
                        boardFull = 1
                if wincount == self.n:
                    print("row win")
                    return (TicTacToe.Row, i, self.turn)
            elif self.board[i] == 0:
                boardFull = 1

        if boardFull == 0:
            print("not full")
            return (TicTacToe.StaleMate, 0, 0)
        else:
            print("false win")

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
        print (self.is_win())

        if outstream:
            self.show()

        temp = 0
        # while self.is_win() == False:
        while self.is_win() == False and temp < 5:
            if outstream:
                self.show()
            temp += 1




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

    pass


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
        print("args.play")
        t.reset(state)
        print("args.play2")

        t.play(outstream=sys.stdout)
        # t.play()

    elif args.mc:
        (games, one, two, stale) = mc(state, args.mc)
        print("%d trials: 1 wins %.2f, "
              "-1 wins %.2f, stalemates %.2f" % (games, one, two, stale))
