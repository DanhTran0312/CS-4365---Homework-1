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

ROW = 3
COL = 3
MAX_DEPTH = 10

class Node:
    def __init__(self, value : int or str, position : tuple):
        self.value = value
        self.position = position
    

class State:
    def __init__(self):
        self.board = [[Node(0, (0, 0)) for i in range(COL)] for j in range(ROW)]


if len(sys.argv) != 3:
    print("Please enter the command in the following format: \npython homework1.py <algorithm_name> <input_file_path>")
    sys.exit(1)

algorithm_name = sys.argv[1]
input_file_path = sys.argv[2]

if algorithm_name not in ["dfs", "ids", "astar1", "astar2"]:
    print("Invalid algorithm name")
    sys.exit(1)

# Read input file
with open(input_file_path, "r") as f:
    input_list = f.readlines()
    for i in range(len(input_list)):
        input_list[i] = input_list[i].strip()
        

