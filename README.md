# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Naked twins can be defined as two boxes of same unit with same value and length of the value in the box is 2. For example, '23' in A1 and '23' in I1 are naked twins in the unit ['A1','B1'....''H1','I1']. As the possible solutions for above example would be A1 as '2' and I1 as '3' or A1 as '3' and I1 as '2', we can eliminate '2' and '3' from all the other boxes in same unit like B1 to H1. This strategy as a constraint can reduce the search space there by optimizes time to arrive at a solution. The best place to call the naked_twins() method is in reduce_puzzle() along with other constraint strategies. The naked_twins is called every time in the search()-->reduce_puzzle() to deduce the search space and to propagate the constraint.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Just like the row, column and square units. We can define the diagonal units and add them to unit list. Therefore the diagonal boxes will have 4 units and non-diagonal boxes will have 3 units. In eliminate() method and only_choice() strategies, the diagonal units constraint will be applied. There by resulting us with diagonal sudoku.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the `assign_value` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login) for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

