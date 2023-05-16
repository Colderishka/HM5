from calculator import Calculator
import pytest

@pytest.mark.parametrize( 'num1, num2, result', [ (4,5,9) ])
def test_sum_positive_nums(num1, num2, result):
    calculator = Calculator()
    res = calculator.sum(num1,num2)
    assert res == result


def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, 6)
    assert res == 0


def test_sum_float():
    calculator = Calculator()
    res = calculator.sum(5.6, 4.3)
    res = round(res, 1)
    assert res == 9.9


def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        res = calculator.div(10, 0)

def test_div():
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_avg_empty_list():
    calculator = Calculator()
    numbers = []
    res = calculator.avg(numbers)
    assert res == 0

def test_avg_positive():
    calculator = Calculator()
    numbers = [1,2,3,4,5,6,7,8,9,5]
    res = calculator.avg(numbers)
    assert res == 5