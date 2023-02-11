# Danh Tran - 2023
# CS 4365 - Assignment 1

import sys
import copy
import heapq

ROW = 3
COL = 3
MAX_DEPTH = 10
count = 0

# Class to represent a state of the board
# board: 2D list of the board
# current_position: tuple of the current position of the empty tile
# cost: total cost of the state
# parent: parent state
# depth: depth of the state
class State:
    def __init__(self, board: list = [[None for _ in range(COL)] for _ in range(ROW)]):
        self.board = board
        self.current_position: tuple = None
        self.cost = 0
        self.parent = None
        self.depth = 0

    # Heuristic 1: Number of misplaced tiles
    # Return the number of misplaced tiles
    def heuristic1(self):
        cost = 0
        for i in range(ROW):
            for j in range(COL):
                if self.board[i][j] != GOAL_STATE.board[i][j] and self.board[i][j] != "*":
                    cost += 1
        return cost

    # Heuristic 2: Manhattan distance
    # Return the sum of the Manhattan distances of the tiles from their goal positions
    def heuristic2(self):
        cost = 0
        for i in range(ROW):
            for j in range(COL):
                if self.board[i][j] != GOAL_STATE.board[i][j] and self.board[i][j] != "*":
                    x, y = GOAL_STATE_POSITIONS[self.board[i][j]]
                    cost += abs(x - i) + abs(y - j)
        return cost

    # Move the tile at the given position to the empty tile
    def move(self, new_position: tuple):
        x, y = self.current_position
        new_x, new_y = new_position
        self.board[x][y], self.board[new_x][new_y] = self.board[new_x][new_y], self.board[x][y]
        self.current_position = new_position

    # Get the total cost of the state based on the heuristic function
    def get_cost(self, heuristic):
        if heuristic == 1:
            return self.heuristic1() + self.depth
        elif heuristic == 2:
            return self.heuristic2() + self.depth
        else:
            return 0

    # Print the board
    def __str__(self) -> str:
        return "\n".join([" ".join([str(self.board[i][j]) for j in range(COL)]) for i in range(ROW)])

    # Compare the cost of two states
    def __lt__(self, o: object) -> bool:
        return self.cost < o.cost

    # Compare if two states are equal based on the board
    def __eq__(self, o: object) -> bool:
        return str(self) == str(o)

    # Hash the state based on the board
    def __hash__(self) -> int:
        return hash(str(self))

    def is_goal(self):
        return self == GOAL_STATE

    # Get the possible moves from the current state
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

# Goal state
GOAL_STATE = State([[7, 8, 1], [6, '*', 2], [5, 4, 3]])
# Dictionary to store the goal position of each tile
GOAL_STATE_POSITIONS = {
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "7": (0, 0),
    "8": (1, 0),
    "*": (2, 0)
}

def dfs(state: State, depth: int, visited: set, moves: list, max_depth: int = MAX_DEPTH):
    global count
    count += 1
    if state.is_goal(): # check if the state is the goal state
        moves.append(state) # add the goal state to the list of moves
        return state, moves # return the goal state and the list of moves
    if depth == max_depth: # if the max depth is reached, return None
        return None
    if state in visited: # if the state has been visited, return None
        return None
    new_visited = copy.deepcopy(visited) # create a deep copy of the new visited set
    new_visited.add(state) # add the current state to the new visited set
    new_moves = copy.deepcopy(moves) # create a new list of moves
    new_moves.append(state) # add the current state to the list of moves
    for move in state.get_possible_moves(): # for each possible move
        new_state = copy.deepcopy(state) # create a new state
        new_state.move(move) # move the new state
        result = dfs(new_state, depth+1, new_visited, new_moves, max_depth) # perform DFS with the new state
        # increment the counter
        if result is not None: # if the result is not None, return the result
            return result
    return None # if the result is None, return None


def ids(state: State):
    for depth in range(0, MAX_DEPTH+1):
        result = dfs(state, 0, set(), [], depth)
        if result is not None:
            return result
    return None

# A* search using two different suitable heuristics
# heuristic 1: number of misplaced tiles in the board
# heuristic 2: sum of manhattan distances of each tile from its goal position
# f(n) = g(n) + h(n) where g(n) is the number of moves from start to n and h(n) is the heuristic value

def astar(state: State, heuristic: int):
    # initialize variables
    global count
    visited = set()
    queue = []
    heapq.heappush(queue, state)
    count += 1
    # while queue is not empty
    while len(queue) > 0:
        # get current state
        current_state = heapq.heappop(queue)
        # if current state is the goal state
        if current_state.is_goal():
            # get path to goal state
            moves = []
            while current_state is not None:
                moves.append(current_state)
                current_state = current_state.parent
            moves.reverse()
            return current_state, moves
        # if current state has been visited
        if current_state in visited:
            # continue
            continue
        # add current state to visited
        visited.add(current_state)
        # for each possible move
        for pos in current_state.get_possible_moves():
            # create new state
            new_state = copy.deepcopy(current_state)
            # move new state
            new_state.move(pos)
            # set parent of new state
            new_state.parent = current_state
            # set depth of new state
            new_state.depth = current_state.depth + 1
            # if new state depth is greater than max depth
            if new_state.depth > MAX_DEPTH:
                continue
            # set cost of new state
            new_state.cost = new_state.get_cost(heuristic)
            # push new state to queue
            heapq.heappush(queue, new_state)
            count += 1
    # if queue is empty
    return None


def main():
    global count

    # sample usage
    # python3 homework1.py dfs 8 * 3 7 1 6 5 2 4
    # Check if the input is valid
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
        input_list = f.readline().split(" ")
        state = State()
        for i in range(ROW):
            for j in range(COL):
                state.board[i][j] = input_list[i*COL+j]
                if state.board[i][j] == "*":
                    state.current_position = (i, j)

    if algorithm_name == "ids":
        res = ids(state)
    elif algorithm_name == "dfs":
        res = dfs(state, 0, set(), [])
    elif algorithm_name == "astar1":
        res = astar(state, 1)
    elif algorithm_name == "astar2":
        res = astar(state, 2)
    else:
        print("Invalid algorithm name")
        sys.exit(1)

    if res is None:
        print("No solution found: Maximum depth reached")
    else:
        for i in res[1]:
            print(i)
            print()
        print("Solution found")
        print("Number of moves: ", len(res[1])-1)
        print("Number of states enqueued: ", count)

if __name__ == "__main__":
    main()
