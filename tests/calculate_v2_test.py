from calculate_v2 import CalculateV2
import pytest


@pytest.fixture
def calculate_v2():
    return CalculateV2()


class TestCalculateV2(object):

    def test_add(self, calculate_v2):

        add = calculate_v2.add(1, 2)

        assert 3 == add

    def test_substract(self, calculate_v2):

        sub = calculate_v2.substract(10, 2)

        assert 8 == sub

    def test_multiply(self, calculate_v2):

        mul = calculate_v2.multiply(10, 9)

        assert 90 == mul

    def test_divide(self, calculate_v2):

        div = calculate_v2.divide(6, 2)

        assert 3 == div
