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

    def test_answer(self):
        assert self.func(3) == 4