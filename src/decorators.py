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
                res = func(*args)

            except Exception as e:
                result = f"{func.__name__} error: {e}. Inputs: {args}"
                res = "Ошибка ввода аргументов"
            else:
                result = f"{func.__name__} ok, Inputs: {args}"

            if filename is None:
                print(result)
            else:
                with open(filename, "a") as file:
                    file.write(result + "\n")
            return res

        return wrapper

    return decorator
