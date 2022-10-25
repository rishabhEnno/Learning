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
    
    @pytest.mark.parametrize("test_input, expected", [(50,51), (54,55)])
    def test_max_space_wardrobe_50(self, test_input, expected):
        assert self.func(test_input) == expected