'''
Write a program to solve the 8-puzzle problem using each of the following algorithms:
1. Depth-first search (25 points)
2. Iterative deepening search (25 points)
3. A* search using two different suitable heuristics (40 points)
10 points for analysis section described on the next page.
Your program should read the initial board configuration from any standard input and print to the
standard output a sequence of board positions that solves the puzzle (only the path to goal from start),
the total number of moves and the total number of search states enqueued.
For each of the above algorithms, expand the search only until depth 10, root being at depth 0. If goal
state is not reached before or at depth 10, then return a failure message. Example, consider the given
input and corresponding output sequence.
Input (Any random position of the tiles):
6 7 1
8 2 *
5 4 3
Output (List of states starting from input to goal state, if found):
6 7 1 (Initial input state)
8 2 *
5 4 3
6 7 1
8 * 2
5 4 3
6 7 1
* 8 2
5 4 3
* 7 1
6 8 2
5 4 3
7 * 1
6 8 2
5 4 3
7 8 1 (Goal state)
6 * 2
5 4 3
Number of moves = 5
Number of states enqueued = 191
Note: * represents an empty tile
What to turn in: Your code and a readme file for compiling the code. The readme file should contain the
following things:
1. Instructions on how to run the program
2. Sample input and its corresponding output
3. Provide a short comparative analysis of two heuristics used for A* (10 points)
Please make sure your readme file gives clear instructions on how to run the code.
For example: python homework1.py <algorithm_name> <input_file_path>
'''

import sys
import copy

ROW = 3
COL = 3
MAX_DEPTH = 10
GOAL_STATE = """7 8 1
6 * 2
5 4 3"""


class State:
    def __init__(self):
        self.board = [[None for _ in range(COL)] for _ in range(ROW)]
        self.current_position : tuple = None

    def move(self, new_position: tuple):
        x, y = self.current_position
        new_x, new_y = new_position
        self.board[x][y], self.board[new_x][new_y] = self.board[new_x][new_y], self.board[x][y]
        self.current_position = new_position
    
    def get_possible_moves(self):
        x, y = self.current_position
        moves = []
        if x > 0:
            moves.append((x-1, y))
        if x < ROW-1:
            moves.append((x+1, y))
        if y > 0:
            moves.append((x, y-1))
        if y < COL-1:
            moves.append((x, y+1))
        return moves

    def __str__(self) -> str:
        return "\n".join([" ".join([str(self.board[i][j]) for j in range(COL)]) for i in range(ROW)])


if len(sys.argv) != 3:
    print("Please enter the command in the following format: \npython homework1.py <algorithm_name> <input_file_path>")
    sys.exit(1)

algorithm_name = sys.argv[1]
input_file_path = sys.argv[2]

if algorithm_name not in ["dfs", "ids", "astar1", "astar2"]:
    print("Invalid algorithm name")
    sys.exit(1)

# Read input file and store it in the initial state
with open(input_file_path, "r") as f:
    input_list = f.readlines()
    state = State()
    for i in range(ROW):
        for j, value in enumerate(input_list[i].split()):
            state.board[i][j] = value
            if (value == "*"):
                state.current_position = (i, j)

def is_goal(state: State):
    return str(state) == GOAL_STATE

def dfs(state: State, depth: int, visited: set, moves: list, max_depth: int = MAX_DEPTH):
    if is_goal(state):
        moves.append(state)
        return state, moves
    if depth == max_depth:
        return None
    if str(state) in visited:
        return None
    new_visited = copy.deepcopy(visited)
    new_visited.add(str(state))
    new_moves = copy.deepcopy(moves)
    new_moves.append(state)
    for move in state.get_possible_moves():
        new_state = copy.deepcopy(state)
        new_state.move(move)
        result = dfs(new_state, depth+1, new_visited, new_moves, max_depth)
        if result is not None:
            return result
    return None


def ids(state: State):
    for depth in range(0, MAX_DEPTH+1):
        result = dfs(state, 0, set(), [], depth)
        if result is not None:
            return result
    return None


if algorithm_name == "ids":
    res = ids(state)


if res is not None:
    state, moves = res
    for move in moves:
        print(move)
    print("Number of moves = {}".format(len(moves)-1))