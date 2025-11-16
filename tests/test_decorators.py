import pytest


from src.decorators import log


def test_log_console(capsys):
    @log()
    def my_function(a, b):
        return a + b

    my_function(2, 3)
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out


def test_log():
    with pytest.raises(Exception, match="my_function"):
        my_function("10", 3)
