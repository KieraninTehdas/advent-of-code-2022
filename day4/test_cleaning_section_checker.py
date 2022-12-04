import unittest

import cleaning_section_checker


class TestCleaningSectionChecker(unittest.TestCase):
    def test_ranges_overlap(self):
        self.assertTrue(cleaning_section_checker._ranges_overlap([2, 8], [3, 7]))
        self.assertTrue(cleaning_section_checker._ranges_overlap([3, 7], [2, 8]))
        self.assertTrue(cleaning_section_checker._ranges_overlap([3, 3], [3, 3]))
        self.assertTrue(cleaning_section_checker._ranges_overlap([3, 3], [3, 7]))
        self.assertTrue(cleaning_section_checker._ranges_overlap([3, 7], [3, 3]))
        self.assertFalse(cleaning_section_checker._ranges_overlap([3, 3], [4, 9]))
        self.assertFalse(cleaning_section_checker._ranges_overlap([1, 6], [4, 9]))

    def test_find_duplicated_assignments(self):
        self.assertEqual(
            2, cleaning_section_checker.find_dupicated_assignments("test_input.txt")
        )


if __name__ == "__main__":
    unittest.main()
