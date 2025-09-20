import unittest


# Реализация
def bin_guess_number(target: int, lst: list) -> list:
    '''
    Ищет загаданное число target в списке lst и выводит загаданное число и количество угадываний,
    которое потребовалось для нахождения числа

    :param int target: Загаданное число
    :param list lst: Интервал значений, в котором загадано число target
    :return: Загаданное число и число угадываний
    :rtype: list
    '''
    # Инициализируем переменные интервалов поиска l, r:
    l, r = 0, len(lst)
    # Инициализируем переменную подсчета количества угадываний:
    cnt = 0
    # Стандартная реализация алгоритма бинарного поиска:
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


def incr_guess_number(target: int, lst: list) -> list:
    '''
    Ищет загаданное число target в списке lst и выводит загаданное число и количество угадываний,
    которое потребовалось для нахождения числа

    :param int target: Загаданное число
    :param list lst: Интервал значений, в котором загадано число target
    :return: Загаданное число и число угадываний
    :rtype: list
    '''
    # Реализуем цикл, который будет проходиться по списку значений:
    for i in range(len(lst)):
        if lst[i] == target:
            return [lst[i], i + 1]


# Тестирование решения
class Test(unittest.TestCase):
    def test_bin_guess_number(self):
        answer = bin_guess_number(17, [1, 2, 5, 7, 8, 11, 16, 17, 20, 21, 57, 100, 101])
        self.assertEqual(answer, [17, 3])

    def test_incr_guess_number(self):
        answer = incr_guess_number(17, [1, 2, 5, 7, 8, 11, 16, 17, 20, 21, 57, 100, 101])
        self.assertEqual(answer, [17, 8])

