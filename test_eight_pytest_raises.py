# pytest -v test_eight_pytest_raises.py
# pip install pytest-reportlog
# pytest -v test_eight_pytest_raises.py --report-log=FILE

import eight_pytest_raises
import pytest

class TestEightPytestRaises:
    def test_add(self):
        assert eight_pytest_raises.add(5, 4) == 9
    def test_subtract(self):
        assert eight_pytest_raises.subtract(9, 3) == 6
    def test_multiply(self):
        assert eight_pytest_raises.multiply(5, 4) == 20
    def test_division(self):
        assert eight_pytest_raises.division(6, 3) == 2
        with pytest.raises(ZeroDivisionError):
            assert eight_pytest_raises.division(4, 0)