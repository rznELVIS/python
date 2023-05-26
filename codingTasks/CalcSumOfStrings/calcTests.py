import unittest
from CalcSumOfStrings.calc import Calc
from parameterized import parameterized


class MyTestCase(unittest.TestCase):
    @parameterized.expand([
        ["10", "11", "21"],
    ])
    def test_something(self, value_1, value_2, expected_result):
        calc: Calc = Calc()

        result: str = calc.add(value_1, value_2)

        # assert
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        [""],
        [" "],
        ["     "],
        [None],
    ])
    def test_first_value_is_incorrect_then_error_is_returned(self, value: str):
        calc: Calc = Calc()

        result: str = calc.add(value, "stub")

        self.assertEqual(result, "Первое значение имеет не корректное значение.")


if __name__ == '__main__':
    unittest.main()
