import unittest

import cleaning_section_checker


class TestCleaningSectionChecker(unittest.TestCase):
    def test_ranges_overlap_completely(self):
        self.assertTrue(
            cleaning_section_checker._ranges_overlap_completely([2, 8], [3, 7])
        )
        self.assertTrue(
            cleaning_section_checker._ranges_overlap_completely([3, 7], [2, 8])
        )
        self.assertTrue(
            cleaning_section_checker._ranges_overlap_completely([3, 3], [3, 3])
        )
        self.assertTrue(
            cleaning_section_checker._ranges_overlap_completely([3, 3], [3, 7])
        )
        self.assertTrue(
            cleaning_section_checker._ranges_overlap_completely([3, 7], [3, 3])
        )
        self.assertFalse(
            cleaning_section_checker._ranges_overlap_completely([3, 3], [4, 9])
        )
        self.assertFalse(
            cleaning_section_checker._ranges_overlap_completely([1, 6], [4, 9])
        )

    def test_ranges_overlap(self):
        self.assertTrue(cleaning_section_checker._ranges_overlap([5, 7], [7, 9]))
        self.assertTrue(cleaning_section_checker._ranges_overlap([7, 9], [5, 7]))
        self.assertTrue(cleaning_section_checker._ranges_overlap([2, 8], [3, 7]))
        self.assertTrue(cleaning_section_checker._ranges_overlap([3, 7], [2, 8]))
        self.assertTrue(cleaning_section_checker._ranges_overlap([6, 6], [4, 6]))
        self.assertTrue(cleaning_section_checker._ranges_overlap([4, 6], [6, 6]))
        self.assertFalse(cleaning_section_checker._ranges_overlap([2, 4], [6, 8]))
        self.assertFalse(cleaning_section_checker._ranges_overlap([6, 8], [2, 4]))
        self.assertFalse(cleaning_section_checker._ranges_overlap([2, 3], [4, 5]))
        self.assertFalse(cleaning_section_checker._ranges_overlap([4, 5], [2, 3]))

    def test_find_duplicated_assignments(self):
        self.assertEqual(
            4, cleaning_section_checker.find_dupicated_assignments("test_input.txt")
        )


if __name__ == "__main__":
    unittest.main()
