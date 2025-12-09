class Currency:
    """ Модель сущности Currency

    Реализует класс с геттерами и сеттерами
    """
    def __init__(self, id: str, num_code: str, char_code: str, name: str, value: int | float, nominal: int):
        """ Конструктор

        :param id: уникальный идентификатор
        :param num_code: цифровой код
        :param char_code: символьный код
        :param name: название валюты
        :param value: курс валюты
        :param nominal: номинал
        """
        # id
        if not isinstance(id, str):
            raise TypeError("Некорректный тип id")
        if not id:
            raise ValueError("Ошибка при задании id валюты")

        # num_code
        if not isinstance(num_code, str):
            raise TypeError("Некорректный тип num_code")
        if not num_code:
            raise ValueError("Ошибка при задании num_code валюты")

        # char_code
        if not isinstance(char_code, str):
            raise TypeError("Некорректный тип char_code")
        if not char_code:
            raise ValueError("Ошибка при задании char_code валюты")

        # name
        if not isinstance(name, str):
            raise TypeError("Некорректный тип name")
        if not name:
            raise ValueError("Ошибка при задании имени валюты")

        # value
        if not isinstance(value, (int, float)):
            raise TypeError("Некорректный тип value")
        if value <= 0:
            raise ValueError("value должно быть положительным числом")

        # nominal
        if not isinstance(nominal, int):
            raise TypeError("Некорректный тип nominal")
        if nominal < 1:
            raise ValueError("nominal должен быть >= 1")

        self.__id: str = id
        self.__num_code: str = num_code
        self.__char_code: str = char_code
        self.__name: str = name
        self.__value: int | float = value
        self.__nominal: int = nominal

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

    @property
    def num_code(self):
        return self.__num_code

    @num_code.setter
    def num_code(self, num_code: str):
        if not isinstance(num_code, str):
            raise TypeError("Некорректный тип num_code")
        if not num_code:
            raise ValueError("Ошибка при задании num_code валюты")
        self.__num_code = num_code

    @property
    def char_code(self):
        return self.__char_code

    @char_code.setter
    def char_code(self, char_code: int):
        if not isinstance(char_code, str):
            raise TypeError("Некорректный тип char_code")
        if not char_code:
            raise ValueError("Ошибка при задании char_code валюты")
        self.__char_code = char_code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Некорректный тип name")
        if not name:
            raise ValueError("Ошибка при задании имени валюты")
        self.__name = name

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int | float):
        if not isinstance(value, (int, float)):
            raise TypeError("Некорректный тип value")
        if value <= 0:
            raise ValueError("value должно быть положительным")
        self.__value = float(value)

    @property
    def nominal(self):
        return self.__nominal

    @nominal.setter
    def nominal(self, nominal):
        if not isinstance(nominal, int):
            raise TypeError("Некорректный тип nominal")
        if nominal < 1:
            raise ValueError("nominal должен быть >= 1")
        self.__nominal = nominal
