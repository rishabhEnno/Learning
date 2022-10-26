
import pytest
from kata import func_wardrobe, return_cheapest, fizzbuzz


class TestWardrobe:
    def test_initial_wardrobe_sum(self):
        out = func_wardrobe()
        for i in out:
            print(i)
            assert sum(i) == 250

    def test_restrict_numbers(self):
        out = func_wardrobe()
        for i in out:
            print(i)
            for j in i:
                assert j in (50, 75, 100, 120)
    
    def test_cheapest_option(self):
        out = return_cheapest()
        assert out[1] == 214
        assert out[0] == [75, 75, 100]


class TestFizzBuzz:

    def test_fizz(self):
        assert fizzbuzz(3) == "Fizz"
    
    def test_buzz(self):
        assert fizzbuzz(5) == "Buzz"
    
    def test_fizzbuzz(self):
        assert fizzbuzz(3*5) == "FizzBuzz"
    
    @pytest.mark.parametrize("other", [1, 4, 7])
    def test_other(self, other):
        assert fizzbuzz(other) == other
    