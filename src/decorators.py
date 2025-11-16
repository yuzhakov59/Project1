from time import time
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[..., Any]:
    """
    Декоратор, который логирует время выполнения функции и результат
    в консоль или файл.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any) -> Any:
            try:
                # Код, который может вызвать исключение
                time_1 = time()
                func(*args)
                time_2 = time()

            except Exception as e:
                result = f"{func.__name__} error: {e}. Inputs: {args}"
            else:
                result = f"{func.__name__} ok, start - {time_1:.7f}, stop - {time_2:.7f}"

            if filename is None:
                print(result)
            else:
                with open(filename, "a") as file:
                    file.write(result + "\n")

        return wrapper

    return decorator
