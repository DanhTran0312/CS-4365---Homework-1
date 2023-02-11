## Assignment 1: 8-puzzle

### Requirements

* Python 3.x

### Usage

* Run `python3 homework1.py <algorithm_name> <input_file>` to run the program.

> * `<algorithm_name>` can be `dfs` `ids` `astar1` `astar2`

> * `<input_file>` is the path of the input file

>> * The input file should containing the space separated input state.
>> * For example - 6 7 1 8 2 * 5 4 3

### Example

* Sample input file: 8 1 3 7 * 6 5 2 4
* Run `python3 homework1.py dfs input.txt`

### Output

**The output will include the initial state and the path that it takes to reach the end goal**
```text
8 1 3
7 * 6
5 2 4

8 1 3
7 6 *
5 2 4

8 1 *
7 6 3
5 2 4

8 * 1
7 6 3
5 2 4

* 8 1
7 6 3
5 2 4

7 8 1
* 6 3
5 2 4

7 8 1
6 * 3
5 2 4

7 8 1
6 2 3
5 * 4

7 8 1
6 2 3
5 4 *

7 8 1
6 2 *
5 4 3

7 8 1
6 * 2
5 4 3

Solution found
Number of moves:  10
Number of states enqueued:  1585
```