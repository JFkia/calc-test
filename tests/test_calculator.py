from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 4321
        b = 4321
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 0
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 11
        b = 1
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 11
        assert result == expected


    def test_divide(self):
        # arrange
        a = 4321
        b = 1
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 4321
        assert result == expected

    def test_divide(self):
        # arrange
        a = 4321
        b = 4321
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 0
        assert result == expected

    def test_divide(self):
        # arrange
        a = 4321
        b = 0
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = ZeroDivisionError
        assert result == expected