from calculate import Calculate
import pytest


@pytest.fixture
def calculate():
    return Calculate(1, 2)


class TestCalculate(object):

    def test_add(self, calculate):

        add = calculate.add()

        assert 3 == add

    def test_substract(self, calculate):

        sub = calculate.substract()

        assert -1 == sub

    def test_multiply(self, calculate):

        mul = calculate.multiply()

        assert 2 == mul

    def test_divide(self, calculate):

        div = calculate.divide()

        assert 0.5 == div