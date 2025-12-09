class UserCurrency:
    """ Модель сущности UserCurrency

    Реализует класс с геттерами и сеттерами, а также связь «много ко многим» между пользователями и валютами.
    """
    def __init__(self, id: str, user_id: str, currency_id: str):
        """ Конструктор

        :param id: уникальный идентификатор
        :param user_id: внешний ключ к User
        :param currency_id: внешний ключ к Currency
        """
        # id
        if not isinstance(id, str):
            raise TypeError("Некорректный тип id")
        if not id:
            raise ValueError("Некорректное значение id")

        # user_id
        if not isinstance(user_id, str):
            raise TypeError("Некорректный тип user_id")
        if not user_id:
            raise ValueError("Некорректное значение user_id")

        # currency_id
        if not isinstance(currency_id, str):
            raise TypeError("Некорректный тип currency_id")
        if not currency_id:
            raise ValueError("Некорректное значение currency_id")

        self.__id = id
        self.__user_id = user_id
        self.__currency_id = currency_id

    # id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        if not isinstance(id, str):
            raise TypeError("Некорректный тип id")
        if not id:
            raise ValueError("Некорректное значение id")

        self.__id = id

    # user_id
    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id: str):
        if not isinstance(user_id, str):
            raise TypeError("Некорректный тип user_id")
        if not user_id:
            raise ValueError("Некорректное значение user_id")

        self.__user_id = user_id

    # currency_id
    @property
    def currency_id(self):
        return self.__currency_id

    @currency_id.setter
    def currency_id(self, currency_id: str):
        if not isinstance(currency_id, str):
            raise TypeError("Некорректный тип currency_id")
        if not currency_id:
            raise ValueError("Некорректное значение currency_id")

        self.__currency_id = currency_id
