import logging
import math
import sys
from typing import Callable
import functools

logging.basicConfig(
    filename="quadratic.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)


def logger(func: Callable=None, *, handle=sys.stdout) -> Callable:
    """ Параметризуемый декоратор, который ведёт логирование в зависимости от аргумента handle

    :param func: декорируемая функция
    :param handle: поток вывода (куда будет произведено логирование)
    :return: возвращает задекорированную функцию
    :rtype: Callable
    """
    if func is None:
        return lambda func: logger(func, handle=handle)

    def log_info(message: str):
        """ Печатает сообщение message о выполнении кода с учётом потока handle (логирование)

        :param message: сообщение, которое печатается
        """
        if isinstance(handle, logging.Logger):
            handle.info(message)
        else:
            handle.write("INFO: " + message + "\n")

    def log_error(message: str):
        """ Печатает сообщение message об ошибке с учётом потока handle (логирование)

        :param message: сообщение, которое печатается
        """
        if isinstance(handle, logging.Logger):
            handle.error(message)
        else:
            handle.write("ERROR: " + message + "\n")

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        """ Функция обёртка

        Логируется сообщение о выполнении кода, дальше в зависимости от результата выполнения
        сообщается об успешном выполнении или выбрасывается исключение об ошибке
        """
        log_info(f"Execute: {func.__name__} args={args}, kwargs={kwargs}")

        try:
            result = func(*args, **kwargs)
            log_info(f"Success: {func.__name__} -> {result}")
            return result

        except Exception as e:
            log_error(f"Exception in {func.__name__}: {type(e).__name__}: {e}")
            raise e

    return wrapper


@logger(handle=sys.stdout)
def solve_quadratic(a, b, c):
    logging.info(f"Solving equation: {a}x^2 + {b}x + {c} = 0")

    # Ошибка типов
    for name, value in zip(("a", "b", "c"), (a, b, c)):
        if not isinstance(value, (int, float)):
            logging.error(f"Parameter '{name}' must be a number, got: {value}")
            raise TypeError(f"Coefficient '{name}' must be numeric")

    # Ошибка: a == 0, b == 0
    if a == 0 and b == 0:
        logging.critical("The equation doesn't make sense")
        raise ValueError("a and b cannot be zero")

    # Ошибка a == 0
    if a == 0:
        logging.error("Coefficient 'a' cannot be zero")
        raise ValueError("a cannot be zero")

    d = b*b - 4*a*c
    logging.debug(f"Discriminant: {d}")

    if d < 0:
        logging.warning("Discriminant < 0: no real roots")
        return None

    if d == 0:
        x = -b / (2*a)
        logging.info("One real root")
        return (x,)

    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    logging.info("Two real roots computed")
    return root1, root2


# solve_quadratic(1, 0, 2)
