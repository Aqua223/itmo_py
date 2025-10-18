from timeit import *
import matplotlib.pyplot as plt
from task_3 import sol as sol3

# IMPORTANT: Read this before checking the code!!!

# Since my iterative building tree algorithm (task_5/sol.py) converts the binary tree type from list to dict,
# timeit module also takes into account the execution time of the function convert(). Due to this after the timing
# iterative implementation works slower than recursive one. So I have pasted my code with iterative implementation
# here with some refactoring, which includes removing of function convert() to not count extra time. That will
# provide my code to execute correctly.


def gen_bin_tree(root: int, height: int) -> list:
    """ Builds the binary tree based on the parameters

    Iteratively builds a binary tree as a list with the root and height according to the rule:
    <left_leaf = root*3, right_leaf = root+4>

    :param int root: Root value of the tree
    :param int height: Height of the tree
    :return: binary tree
    :rtype: dict
    """
    # Initializing an empty binary tree as a list with 2 ** height - 1 elements (height starts with 1)
    tree_lst = [root for _ in range(2 ** height - 1)]
    # (i - 1) // 2 - parent of the note
    for i in range(1, 2 ** height - 1):
        tree_lst[i] = tree_lst[(i - 1) // 2] * 3 if i % 2 else tree_lst[(i - 1) // 2] + 4

    return tree_lst


gen_bin_tree_iterative = gen_bin_tree
gen_bin_tree_recursive = sol3.gen_bin_tree


def timing(root: int, height: int, option: int) -> float:
    """ Evaluates a minimum execution time of the algorithm

    With the module timeit computes the overall execution time for number (number = 1000) operations repeat (repeat = 5)
    times then returns the minimum of the execution times of the final list divided by operations number for iterative
    algorithm if the option parameter set to 0 and for recursive algorithm if set to 1

    :param int root: root value of the tree
    :param int height: height of the tree
    :param int option: variable that indicates which type of algorithm will be measured
    :return: minimum execution time of the algorithm
    :rtype: float
    """
    # Number of operations
    number = 50
    # Result
    res = None

    if not option:
        res = min([t for t in repeat("gen_bin_tree_iterative(%d, %d)" % (root, height),
                                     number=number, globals=globals())]) / number
    else:
        res = min([t for t in repeat("gen_bin_tree_recursive(%d, %d)" % (root, height),
                                     number=number, globals=globals())]) / number

    return res


# List of numbers for which we will find the corresponding binary trees
heights = range(1, 15)
# Root
r = 2

# Evaluating execution times for each algorithm
iterative_times = [timing(r, height, option=0) for height in heights]
recursive_times = [timing(r, height, option=1) for height in heights]

# Plotting the asymptotics of the algorithms
plt.plot(heights, iterative_times, label='Iterative binary tree')
plt.plot(heights, recursive_times, label='Recursive binary tree')
plt.xlabel('Values of heights')
plt.ylabel('Execution time')
plt.title('Comparison the execution time between iterative and recursive algorithms of building binary tree')
plt.legend()
plt.grid(True)
plt.show()

# Summary: iterative implementation works faster than recursive one
