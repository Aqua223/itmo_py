import unittest


def guess_number(target: int, lst: list) -> list:
    ''' Ищет загаданное число target в списке lst и выводит загаданное число и количество итераций,
    которое потребовалосьдля нахождения числа

    :param target:
    :param lst:
    :return:
    '''
    l, r = 0, len(lst)
    cnt = 0
    while r - l > 1:
        cnt += 1
        mid = (l + r) // 2
        if lst[mid] <= target:
            l = mid
            if lst[mid] == target:
                break
        else:
            r = mid

    return [lst[l], cnt]


class Test(unittest.TestCase):
    def test_guess_number(self):
        answer = guess_number(17, [1, 2, 5, 7, 8, 11, 16, 17, 20, 21, 57, 100, 101])
        self.assertEqual(answer, [17, 3])


print(guess_number(17, [1, 2, 5, 7, 8, 11, 16, 17, 20, 21, 57, 100, 101]))
help(guess_number(1, [1, 2]))