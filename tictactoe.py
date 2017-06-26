from copy import deepcopy
import random


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
    print state.board


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


def random_move(s):
    nps = next_positions(s)
    return nps[int(random.random()*len(nps))]

    # loops = [
    #     [0, 0], [0, 1], [0, 2],
    #     [1, 0], [1, 1], [1, 2],
    #     [2, 0], [2, 1],  [2, 2]
    # ]
    # steps = int(random.random()*9)
    # while s.board[loops[steps % 9][0]][loops[steps % 9][1]] is not None:
    #     steps += 1
    #
    # s.board[loops[steps][0]][loops[steps][1]] = 2
    return s


def computer_move(s, kind='random'):
    if kind == 'random':
        return random_move(s)
    else:
        return s


def did_win(s):

    if (s.board[2][0] == s.board[1][1] and s.board[0][2] == s.board[2][0]):
        return True
    if (s.board[0][0] == s.board[1][1] and s.board[2][2] == s.board[0][0]):
        return True
    for i in range(3):
        if (s.board[i][0] == s.board[i][1] and s.board[i][0] == s.board[i][2]):
            return True
        if (s.board[0][i] == s.board[1][i] and s.board[0][i] == s.board[2][i]):
            return True
        return False


s = State([
    [1, 1, None],
    [1, 1, None],
    [0, None, None]], 1)
print_state(s)
np = next_positions(s)
[print_state(n) for n in np]
print "test win"
print did_win(s)

print "random move"
print_state(s)
s = random_move(s)
print print_state(s)
print print_state(random_move(s))
# print "test next pos"
# print next_positions(s)
