
import pytest
from kata import func_wardrobe, return_cheapest


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