import unittest

import rock_paper_scissors

# Rock (A), Paper(B), Scissors(C)


class TestRockPaperScissors(unittest.TestCase):
    def setUp(self):
        self.game = rock_paper_scissors.Game("test_input.txt")

    def test_calculate_your_play(self):
        self.assertEqual(self.game._calculate_your_play("A", "X"), "C")
        self.assertEqual(self.game._calculate_your_play("A", "Y"), "A")
        self.assertEqual(self.game._calculate_your_play("A", "Z"), "B")

    def test_round_score(self):
        self.assertEqual(8, self.game._calculate_round_score("A", "Z"))
        self.assertEqual(1, self.game._calculate_round_score("B", "X"))
        self.assertEqual(6, self.game._calculate_round_score("C", "Y"))
        self.assertEqual(7, self.game._calculate_round_score("C", "Z"))
        self.assertEqual(3, self.game._calculate_round_score("A", "X"))

    def test_total_score(self):
        self.assertEqual(12, self.game.total_score())


if __name__ == "__main__":
    unittest.main()
