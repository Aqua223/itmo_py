# Реализация

def gen_bin_tree(root: int, height: int) -> dict[int, list]:
    ''' Рекурсивно строит бинарное дерево с корнем root и высотой height по правилу:
    <left_leaf = root*3, right_leaf = root+4>

    :param int root: Значение в корне бинарного дерева
    :param int height: Высота бинарного дерева
    :return: Возвращает бинарное дерево
    :rtype: dict
    '''
    # Обозначим конец рекурсии
    if height == 1:
        return {root: []}

    # Найдём рекурсивно дочерние вершины
    left = gen_bin_tree(root * 3, height - 1)
    right = gen_bin_tree(root + 4, height - 1)

    # Возвращаем дерево
    return {root: [left, right]}


def helper() -> None:
    '''
    Реализует пользовательский ввод данных для проверки решения
    '''
    try:
        # Инициализируем переменные
        root, height = 2, 6
        status = int(input('Введите 1 для инициализации корня и высоты бинарного дерева или 0, если '
                           'хотите оставить значения по умолчанию: '))
        if status == 1:
            root, height = map(int, input("Введите значения корня и высоты бинарного дерева через запятую: ").split(','))
            if height < 1:
                print('-' * 100)
                print("Некорректное значние для height (height > 0)")
                print('-' * 100)
                return

        elif status != 0:
            print('-' * 100)
            print("Некорректное значние для status")
            print('-' * 100)
            return
        # Построим дерево:
        print('-' * 100)
        tree = gen_bin_tree(root, height)
        print(tree)
        # Проверим наличие элемента в списке
        print('-' * 100)

    except ValueError:
        print("Некорректный формат данных")

