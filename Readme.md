# Task 1. Data Structures. Sorting. Working with a Singly Linked List
In this project, we developed a data structure called a singly linked list and implemented various operations on it, such as insertion, deletion, element search, as well as reversing, sorting, and merging sorted lists.

`ex_1.py`: This file contains the definitions of the Node and LinkedList classes, which represent nodes and the singly linked list, respectively. The defined methods include inserting at the beginning and end of the list, inserting after a given node, deleting a node by key value, searching for an element by value, displaying the list, and methods for reversing, sorting, and merging lists.

# Task 2. Recursion. Creating a Pythagoras Tree Fractal Using Recursion
This Python program uses recursion to create a Pythagoras tree fractal. The Pythagoras tree fractal looks like a tree where each branch splits into two smaller branches, forming a 45-degree angle with the main branch.

### Requirements
Python 3.x
Turtle module (standard Python module)
### How to Use
- Run the program using the command python `ex_2.py.`
- Enter the recursion level (an integer) to set the complexity of the Pythagoras tree fractal.
- Press any key or click the mouse in the window to close the fractal display window.
  
# Task 3. Trees, Dijkstra's Algorithm
This file contains the implementation of Dijkstra's algorithm in Python using a binary heap to find the shortest paths in a weighted graph. This implementation works only with graphs that do not have negative edge weights.

### Usage
Run Python, importing the `dijkstra` function from the `ex_3.py` file.
Define the graph for which you need to find the shortest paths.
Call the `dijkstra(graph, start_vertex)` function, passing the graph and the start vertex.
### Example
```python
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_vertex = 'A'
print(dijkstra(graph, start_vertex))
```
# Task 4. Heap Visualization
In this task, we use Python to build and visualize a binary heap using the NetworkX and Matplotlib libraries.

The given code in the `ex_4.py` file implements the construction of binary trees and their visualization.

The task is to modify this code to build and visualize a maximum binary heap.

### Dependencies
Python 3.x
Libraries:
NetworkX
Matplotlib
Install the libraries using pip:

```bash
pip install networkx matplotlib
```
# Task 5. Binary Tree Traversal Visualization
This project contains code for visualizing a binary tree using the NetworkX and Matplotlib libraries. The project also implements depth-first search (DFS) and breadth-first search (BFS) traversals, which are demonstrated on the visualized tree.

### Requirements
Before running the code, make sure the following packages are installed:

Python (recommended version 3.x)
NetworkX
Matplotlib
You can install these packages using pip:

``` bash
pip install networkx matplotlib
```
### Color Explanation
In the visualization, each node has its own color, which is marked in the traversal order. Colors are generated automatically so that each node has a unique color.

# Task 6: Greedy Algorithms and Dynamic Programming
This task involves writing a Python program that implements two approaches — a greedy algorithm and a dynamic programming algorithm for selecting food items with the highest total calorie content within a limited budget.

In this task, a dictionary `items` is provided, containing data on various types of food. Each type of food is represented as a dictionary with cost and calorie content. The task is to select certain types of food so that their total calorie content is maximized, but the total cost does not exceed the limited budget.

### Greedy Algorithm
In the greedy algorithm, the list of items is first sorted by their calorie-to-cost ratio, and then items are selected in descending order of this ratio until the total cost exceeds the budget.

### Dynamic Programming Algorithm
In this approach, dynamic programming is used to compute the optimal set of dishes to maximize calorie content within the given budget. A two-dimensional array `k` is created where `k[i][j]` represents the maximum calorie content that can be obtained from the first i items given that the total cost does not exceed j.

# Task 7: Monte Carlo Method
### Task Description
You need to write a Python program that simulates a large number of dice rolls, calculates the sums of the numbers that appear on the dice, and determines the probability of each possible sum. Based on the simulations, create a table or chart that shows the probabilities of each sum as determined by the Monte Carlo method. Compare the obtained results with analytical calculations.

### Simulation Results
### Using the Monte Carlo Method
| Sum | Probability    |
|------|----------------|
| 2    | 2.79% (27870/1000000)   |
| 3    | 5.55% (55479/1000000)   |
| 4    | 8.32% (83248/1000000)   |
| 5    | 11.08% (110804/1000000)  |
| 6    | 13.93% (139259/1000000)  |
| 7    | 16.61% (166148/1000000)  |
| 8    | 13.93% (139282/1000000)  |
| 9    | 11.11% (111142/1000000)  |
| 10   | 8.36% (83584/1000000)   |
| 11   | 5.55% (55533/1000000)   |
| 12   | 2.77% (27651/1000000)   |
### Analytical Results
| Sum | Probability    |
|------|----------------|
| 2    | 2.78% (1/36)   |
| 3    | 5.56% (2/36)   |
| 4    | 8.33% (3/36)   |
| 5    | 11.11% (4/36)  |
| 6    | 13.89% (5/36)  |
| 7    | 16.67% (6/36)  |
| 8    | 13.89% (5/36)  |
| 9    | 11.11% (4/36)  |
| 10   | 8.33% (3/36)   |
| 11   | 5.56% (2/36)   |
| 12   | 2.78% (1/36)   |
### Conclusions
The results of the simulation using the Monte Carlo method closely match the analytical calculations. This confirms the effectiveness of the Monte Carlo method for approximating probabilities in experimental conditions.
