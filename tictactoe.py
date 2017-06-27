from copy import deepcopy
import random
import sys


class State:
    def __init__(self, board, turn=None):
        self.board = board
        self.turn = turn  # 1 or 0


def next_positions(state):
    states = []
    for i in range(3):
        for j in range(3):
            if state.board[i][j] is None:
                b = State(deepcopy(state.board), 1 - state.turn)
                b.board[i][j] = state.turn
                states.append(b)
    return states


def print_state(state):
    print "Player:" + str(state.turn)
    for row in state.board:
        s = ''
        for val in row:
            if val is None:
                s += ' - '
            else:
                s += ' ' + str(val) + ' '
        print s + '\n'


def player_move(state, pos):
    i, j = pos
    b = State(deepcopy(state.board), 1 - state.turn)
    if b.board[i][j] is not None:
        print "position taken"
    b.board[i][j] = state.turn
    return b

# Calculate all possible routes
# and assign a score to all the potential end games
#     - (- to loss and + to win)
#     - the fewer moves to end game should matter as well
#     - (closer to now is more negative)
# choose next moves on the board with highest score
# b = np.matrix([[None, None, None],[None, None, None],[None,None, None]])

# choose minimum from oponents move
#     >> (he always picks the worst for you)
# choose maximum from your move


def minimax(node, depth, maximizing_player):
    if stale_mate(node):
        return 0
    if did_win(node) and maximizing_player:
        return -1000
    if did_win(node) and not maximizing_player:
        return 1000

    if maximizing_player:
        bestValue = -1000
        for child in next_positions(node):
            v = minimax(child, depth - 1, False)
            bestValue = max(bestValue, v)
        # print "best" + str(bestValue)
        return bestValue

    else:
        bestValue = 1000
        for child in next_positions(node):
            v = minimax(child, depth - 1, True)
            bestValue = min(bestValue, v)
        # print "vest" + str(bestValue)
        return bestValue


def best_move(s):
    bestMove = None
    bestMoveScore = -1001
    for b in next_positions(s):
        print minimax(b, 3, False)
        print_state(b)
        # maximizing player is False because we maximize for the computer
        score = minimax(b, 3, False)
        if score > bestMoveScore:
            bestMove = b
            bestMoveScore = score

    return bestMove


def random_move(s):
    nps = next_positions(s)
    return nps[int(random.random()*len(nps))]


def computer_move(s, kind='random'):
    if kind == 'random':
        return random_move(s)

    elif kind == 'minimax':
        return best_move(s)


def did_win(s):
    if (s.board[2][0] is not None) and (s.board[2][0] == s.board[1][1] and s.board[0][2] == s.board[2][0]):
        return True
    if (s.board[0][0] is not None) and (s.board[0][0] == s.board[1][1] and s.board[2][2] == s.board[0][0]):
        return True
    for i in range(3):
        # rows
        if (s.board[i][0] is not None) and (s.board[i][0] == s.board[i][1] and s.board[i][0] == s.board[i][2]):
            return True
        # columns
        if (s.board[0][i] is not None) and (s.board[0][i] == s.board[1][i] and s.board[0][i] == s.board[2][i]):
            return True
    return False


def stale_mate(s):
    if len(next_positions(s)) == 0:
        return True


def play_game():
    # create board
    s = State([
        [None, None, None],
        [None, None, None],
        [None, None, None]], 1)
    print_state(s)
    print did_win(s)
    while not did_win(s) and not stale_mate(s):
        # prompt player
        position = raw_input("Enter position: ")
        x, y = position.split(",")
        s = player_move(s, [int(x), int(y)])
        print_state(s)
        if did_win(s) or stale_mate(s):
            break
        # make computer move
        s = computer_move(s, kind='minimax')
        print_state(s)
    if stale_mate(s):
        print "nobody won!"
    else:
        print "player {} won!".format(s.turn)

# play_game()
s = State([
    [None, 0, 0],
    [None, 1, 0],
    [None, None, 1]], 1)
x = best_move(s)
print_state(x)
# np = next_positions(s)
# [print_state(n) for n in np]
# print "test win"
# print did_win(s)
#
# print "random move"
# print_state(s)
# s = random_move(s)
# print print_state(s)
# print print_state(random_move(s))
# print "test next pos"
# print next_positions(s)
