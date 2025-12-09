class User:
    """ Модель сущности User

    Реализует класс с геттерами и сеттерами
    """
    def __init__(self, id: str, name: str):
        """ Конструктор

        :param id: уникальный идентификатор
        :param name: Имя пользователя
        """
        # id
        if not isinstance(id, str):
            raise TypeError("Некорректный тип id")
        if not id:
            raise ValueError("Ошибка при задании уникального идентификатора")

        # name
        if not isinstance(name, str):
            raise TypeError("Некорректный тип name")
        if not name:
            raise ValueError("Ошибка при задании имени пользователя")

        self.__id: str = id
        self.__name: str = name

    # id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        if not isinstance(id, str):
            raise TypeError("Некорректный тип id")
        if not id:
            raise ValueError("Ошибка при задании уникального идентификатора")
        self.__id = id

    # name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Некорректный тип name")
        if not name:
            raise ValueError("Ошибка при задании имени пользователя")
        self.__name = name
