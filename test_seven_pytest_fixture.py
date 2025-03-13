# learning pytest fixture => setup and teardown
# pytest -v test_seven_pytest_fixture

from seven_pytest_fixture import Person
import pytest
import time
class TestPerson:
    @pytest.fixture     # setup
    def setup(self):
        self.p1 = Person('Hosein', 'Roosta')
        self.p2 = Person('Ali', 'Ahmadi')
        yield 'setup'   # teardown
        print('Done..')  # teardown - print does not work in teardown
        time.sleep(2)   # teardown

    def test_full_name(self, setup):
        assert self.p1.full_name() == 'Hosein Roosta'
        assert self.p2.full_name() == 'Ali Ahmadi'
    def test_email(self, setup):
        assert self.p1.email() == 'HoseinRoosta@gmail.com'
        assert self.p2.email() == 'AliAhmadi@gmail.com'

