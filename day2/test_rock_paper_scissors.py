import unittest

import rock_paper_scissors

# Rock (A), Paper(B), Scissors(C)


class TestRockPaperScissors(unittest.TestCase):
    def setUp(self):
        self.game = rock_paper_scissors.Game("test_input.txt")

    def test_round_score(self):
        self.assertEqual(8, self.game._calculate_round_score("A", "B"))
        self.assertEqual(1, self.game._calculate_round_score("B", "A"))
        self.assertEqual(6, self.game._calculate_round_score("C", "C"))
        self.assertEqual(7, self.game._calculate_round_score("C", "A"))
        self.assertEqual(3, self.game._calculate_round_score("A", "C"))

    def test_total_score(self):
        self.assertEqual(15, self.game.total_score())


if __name__ == "__main__":
    unittest.main()
