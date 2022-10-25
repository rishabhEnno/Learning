import pytest
from kata import func_wardrobe

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
    
    # @pytest.mark.parametrize("test_input", [(50,50,50,50,50), (50, 50, 50, 100), ()])
    # def test_max_space_wardrobe_50(self, test_input):
    #     assert sum(test_input) == 250
    
