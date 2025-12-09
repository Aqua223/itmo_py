class Author:
    """ Модель сущности Author

    Реализует класс с геттерами и сеттерами
    """
    def __init__(self, name: str, group: str = "Р3123"):
        """ Конструктор

        :param name: имя автора
        :param group: учебная группа
        """
        if not isinstance(name, str):
            raise TypeError("Некорректный тип name")

        if not name:
            raise ValueError('Ошибка при задании имени автора')

        if not isinstance(group, str):
            raise TypeError("Некорректный тип group")

        if len(group) != 5:
            raise ValueError('Ошибка при задании имени группы')

        self.__name: str = name
        self.__group: str = group

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Некорректный тип name")

        if not name:
            raise ValueError('Ошибка при задании имени автора')

        self.__name = name

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        if not isinstance(group, str):
            raise TypeError("Некорректный тип group")

        if len(group) != 5:
            raise ValueError('Ошибка при задании имени группы')

        self.__group = group
