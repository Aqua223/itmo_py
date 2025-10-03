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
        mid = (l + r) // 2
        if lst[mid] <= target:
            l = mid
            if lst[mid] == target:
                cnt += 1
                break
        else:
            r = mid
        cnt += 1

    if lst[mid] == target:
        return [lst[l], cnt]
    else:
        return [-1, -1]


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
    return [-1, -1]


def helper() -> None:
    '''
    Реализует пользовательский ввод данных для решения
    '''
    try:
        # Инициализируем переменные
        lst = list(map(int, input("Введите интервал значений через запятую: ").split(',')))
        target = int(input("Введите загаданное число: "))
        print('-' * 100)
        # Поиск перебором
        guessed1, attempts1 = incr_guess_number(target, lst)
        # Проверим наличие элемента в списке
        if guessed1 == -1:
            print('Загаданное число отсутствует в интервале значений')
            print('-' * 100)
            return
        print('Перебор:')
        print(f'\n  Ваше число: {guessed1}\n  Количество угадываний: {attempts1}\n')
        # Бинарный поиск
        if sorted(lst) == lst:
            guessed2, attempts2 = bin_guess_number(target, lst)
            print('Бинарный поиск:')
            print(f'\n  Ваше число: {guessed2}\n  Количество угадываний: {attempts2}')
        else:
            print('Бинарный поиск:')
            print('  Массив не является отсортированным')
        print('-' * 100)

    except ValueError:
        print("Некорректный формат данных")




