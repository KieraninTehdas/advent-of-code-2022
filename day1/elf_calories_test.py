import unittest

import elf_calories


class TestElfRations(unittest.TestCase):
    def setUp(self):
        self.elf_rations = elf_calories.ElfRations("test_input.txt")

    def test_max_calories(self):
        self.assertEqual(24000, self.elf_rations.max_calories())

    def test_top_n_elves_total_calories(self):
        self.assertEqual(45000, self.elf_rations.top_n_elves_total_calories())


if __name__ == "__main__":
    unittest.main()
