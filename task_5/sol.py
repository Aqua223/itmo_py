def left_leaf(parent: int) -> int:
    """ Evaluates the value of the left leaf

    :param parent: value of the parent
    :return: value of the left leaf
    :rtype: int
    """
    return parent * 3


def right_leaf(parent: int) -> int:
    """ Evaluates the value of the right leaf

        :param parent: value of the parent
        :return: value of the right leaf
        :rtype: int
        """
    return parent + 4


def convert(lst: list, height: int) -> dict[int, list]:
    """ Converts a binary tree

    Receives a binary tree as an input in the form of a list and converts it into a dictionary

    :param lst: binary tree as a list
    :param height: height of the tree
    :return: binary tree as a dictionary
    :rtype: dict[int, list]
    """
    dct = []
    # That's kinda complicated, but it works (can be proved by me)
    for i in range(height, 1, -1):
        temp = []
        for j in range(2 ** (i - 1) - 1, 2 ** i - 1, 2):
            if 2 * j + 1 >= 2 ** height - 2:
                temp.append([{lst[j]: []}, {lst[j + 1]: []}])
            else:
                temp.append([{lst[j]: dct[2 ** (i - 1) - 1 - j]}])
                temp.append([{lst[j + 1]: dct[2 ** (i - 1) - j]}])
        dct = temp

    return {lst[0]: sum(dct, [])}


def gen_bin_tree(root: int, height: int) -> dict[int, list]:
    """ Builds the binary tree based on the parameters

    Iteratively builds a binary tree with the root and height according to the rule:
    <left_leaf = root*3, right_leaf = root+4>

    At first creates the binary tree as a list, then converts it to dict with convert()

    :param int root: Root value of the tree
    :param int height: Height of the tree
    :return: binary tree
    :rtype: dict
    """
    # Initializing an empty binary tree as a list with 2 ** height - 1 elements (height starts with 1)
    tree_lst = [root for _ in range(2 ** height - 1)]
    # (i - 1) // 2 - parent of the note
    for i in range(1, 2 ** height - 1):
        tree_lst[i] = left_leaf(tree_lst[(i - 1) // 2]) if i % 2 else right_leaf(tree_lst[(i - 1) // 2])

    # Converting to dict
    dict_list = convert(tree_lst, height)
    return dict_list


def helper() -> None:
    """ Implements user input to verify the solution
    """
    try:
        # Variable initializing
        root, height = 2, 6
        status = int(input("Enter 1 to initialize the root and height of the binary tree, "
                           "or 0 if you want to keep the default values: "))
        if status == 1:
            root, height = map(int, input("Enter the values of the root and height "
                                          "of the binary tree separated by commas: ").split(','))
            if height < 1:
                print('-' * 100)
                print("Invalid value for height (height > 0)")
                print('-' * 100)
                return

        elif status != 0:
            print('-' * 100)
            print("Invalid value for status")
            print('-' * 100)
            return
        # Building a tree
        print('-' * 100)
        tree = gen_bin_tree(root, height)
        print(tree)
        print('-' * 100)

    except ValueError:
        print("Invalid input")

