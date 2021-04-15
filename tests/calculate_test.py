from calculate import Calculate


class TestCalculate(object):

    def test_add(self):

        cal = Calculate(1, 2)
        add = cal.add()

        assert 3 == add

    def test_substract(self):
        cal = Calculate(5, 1)
        sub = cal.substract()

        assert 4 == sub

    def test_multiply(self):
        cal = Calculate(10, 2)
        mul = cal.multiply()

        assert 20 == mul

    def test_divide(self):
        cal = Calculate(10, 2)
        div = cal.divide()

        assert 5 == div