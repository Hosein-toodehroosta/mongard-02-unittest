# pytest -v six_pytest.py

import six_pytest

class Test_six_pytest:
    def test_add(self):
        assert six_pytest.add(5, 7) == 12
        assert six_pytest.add(-1, -5) == -6
    def test_subtract(self):
        assert six_pytest.subtract(4, 5) == -1
        assert six_pytest.subtract(9, 0) == 9
    def test_multiply(self):
        assert six_pytest.multiply(5, 6) != 20
        assert six_pytest.multiply(-5, -6) == 30
    def test_division(self):
        assert six_pytest.division(50, 10) == 5
