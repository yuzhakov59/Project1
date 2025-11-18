import pytest


from src.decorators import log


def test_log_console(capsys):
    @log()
    def my_function(a, b):
        return a + b

    my_function(2, 3)
    captured = capsys.readouterr()
    assert "my_function ok, Inputs: (2, 3)" in captured.out
    assert my_function(2, 3) == 5





def test_log():
    @log()
    def my_function(x, y):
        return x + y

    my_function("10", 3)
    assert my_function("10", 3) == "Ошибка ввода аргументов"


def test_log_file(filename="mylog.txt"):
    """Проверяет, что информация логируется в файл."""
    file_path_str = str(filename)

    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3
    with open(file_path_str, "r") as f:
        assert "my_function ok, Inputs: (1, 2)" in f.read()
