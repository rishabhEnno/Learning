import pytest

# define a function
def func(x):
    return x + 1

# define a test
def test_answer():
    assert func(3) == 4

# define a test class
class TestSomething:
    def func(self, x):
        return x + 1
    
    def func_zero_division_error(self):
        return 1/0

    def test_answer(self):
        assert self.func(3) == 4

    def test_answer_exception(self):
        with pytest.raises(ZeroDivisionError):
            self.func_zero_division_error()