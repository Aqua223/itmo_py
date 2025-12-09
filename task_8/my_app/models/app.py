from .author import Author


class App:
    """ Модель сущности App

    Реализует класс с геттерами и сеттерами
    """
    def __init__(self, name: str, version: str, author: Author):
        """ Конструктор

        :param name: название приложения
        :param version: версия приложения
        :param author: объект Author
        """
        if not isinstance(name, str):
            raise TypeError("Некорректный тип name")
        if not name:
            raise ValueError("Ошибка при задании имени проекта")

        if not isinstance(version, str):
            raise TypeError("Некорректный тип version")
        if not version:
            raise ValueError("Ошибка при задании версии")

        if not isinstance(author, Author):
            raise ValueError('Ошибка при задании имени автора')

        self.__name: str = name
        self.__version: str = version
        self.__author: Author = author

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Некорректный тип name")
        if not name:
            raise ValueError("Ошибка при задании имени проекта")

        self.__name = name

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        if not isinstance(version, str):
            raise TypeError("Некорректный тип version")
        if not version:
            raise ValueError("Ошибка при задании версии")

        self.__version = version

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        if not isinstance(author, Author):
            raise ValueError('Ошибка при задании имени автора')
        else:
            self.__author = author
