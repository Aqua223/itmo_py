from timeit import *
import matplotlib.pyplot as plt


def fact_recursive(n: int) -> int:
    """ Calculates the factorial of the number recursively

    :param n: factorial parameter
    :return: value of the factorial
    :rtype: int
    """
    return n * fact_recursive(n - 1) if n > 1 else 1


def fact_iterative(n: int) -> int:
    """ Calculates the factorial of the number iteratively

    :param n: factorial parameter
    :return: value of the factorial
    :rtype: int
    """
    res = 1
    while n > 1:
        res *= n
        n -= 1

    return res


def timing(n: int, option: int) -> float:
    """ Evaluates a minimum execution time of the algorithm

    With the module timeit computes the overall execution time for number (number = 1000) operations repeat (repeat = 5)
    times then returns the minimum of the execution times of the final list divided by operations number for iterative
    algorithm if the option parameter set to 0 and for recursive algorithm if set to 1

    :param n: factorial parameter
    :param option: variable that indicates which type of algorithm will be measured
    :return: minimum execution time of the algorithm
    :rtype: float
    """
    # Number of operations
    number = 1000
    # Result
    res = None

    if not option:
        res = min([t for t in repeat("fact_iterative(%d)" % n, number=number, globals=globals())]) / number
    else:
        res = min([t for t in repeat("fact_recursive(%d)" % n, number=number, globals=globals())]) / number

    return res


# List of numbers for which we will find the corresponding factorials
numbers = range(1, 100)

# Evaluating execution times for each algorithm
iterative_times = [timing(n, option=0) for n in numbers]
recursive_times = [timing(n, option=1) for n in numbers]

# Plotting the asymptotics of the algorithms
plt.plot(numbers, iterative_times, label='Iterative factorial')
plt.plot(numbers, recursive_times, label='Recursive factorial')
plt.xlabel('Values of N')
plt.ylabel('Execution time')
plt.title('Comparison the execution time between iterative and recursive algorithms of finding a factorial')
plt.legend()
plt.grid(True)
plt.show()
