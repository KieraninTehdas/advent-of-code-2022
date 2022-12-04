import unittest

import rucksack_error_checker


class TestRucksackErrorChecker(unittest.TestCase):
    def test_calculate_priority(self):
        self.assertEqual(1, rucksack_error_checker._calculate_priority("a"))
        self.assertEqual(26, rucksack_error_checker._calculate_priority("z"))
        self.assertEqual(27, rucksack_error_checker._calculate_priority("A"))
        self.assertEqual(52, rucksack_error_checker._calculate_priority("Z"))

    def test_get_compartments(self):
        self.assertEqual(
            rucksack_error_checker._get_compartments("vJrwpWtwJgWrhcsFMMfFFhFp"),
            ("vJrwpWtwJgWr", "hcsFMMfFFhFp"),
        )
        self.assertEqual(
            rucksack_error_checker._get_compartments(
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
            ),
            ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
        )

    def test_find_common_items(self):
        self.assertEqual(
            rucksack_error_checker._find_common_items("vJrwpWtwJgWrhcsFMMfFFhFp"), ["p"]
        )
        self.assertEqual(rucksack_error_checker._find_common_items("aA"), [])

    def test_common_item_priority_total(self):
        self.assertEqual(
            157, rucksack_error_checker.common_item_priority_total("test_input.txt")
        )


if __name__ == "__main__":
    unittest.main()
