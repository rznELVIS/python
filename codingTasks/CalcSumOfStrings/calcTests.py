import unittest
from CalcSumOfStrings.calc import Calc, CalcEncoding
from parameterized import parameterized


class CalcTests(unittest.TestCase):
    @parameterized.expand([
        ["15", "11", "26"],
        ["0", "10", "10"],
        ["0", "0", "0"],
        ["10", "0", "10"],
        ["5", "5", "10"],
    ])
    def test_calc_add_correctly(self, value_1, value_2, expected_result):
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

        result: str = calc.add(value, "100")

        self.assertEqual(result, "Первое значение имеет не корректное значение.")

    @parameterized.expand([
        [""],
        [" "],
        ["     "],
        [None],
    ])
    def test_second_value_is_incorrect_then_error_is_returned(self, value: str):
        calc: Calc = Calc()

        result: str = calc.add("100", value)

        self.assertEqual(result, "Второе значение имеет не корректное значение.")


class CalcEncodingTests(unittest.TestCase):

    @parameterized.expand([
        ["15", "11", "26"],
        ["0", "10", "10"],
        ["0", "0", "0"],
        ["10", "0", "10"],
        ["5", "5", "10"],
    ])
    def test_calc_add_correctly(self, value_1, value_2, expected_result):
        calc: CalcEncoding = CalcEncoding()

        result: str = calc.add(value_1, value_2)

        # assert
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
