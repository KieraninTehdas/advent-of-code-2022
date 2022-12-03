import unittest

import elf_calories


class TestElfCalorieCalculator(unittest.TestCase):
    def test_calorie_calculator(self):
        test_input_filename = "test_input.txt"

        self.assertEqual(24000, elf_calories.find_max_calories(test_input_filename))


if __name__ == "__main__":
    unittest.main()
