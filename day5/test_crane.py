import unittest
import pdb

from collections import deque

import crane


class TestCrane(unittest.TestCase):
    def test_initialise_stacks(self):
        expected = [
            (1, deque("ZN")),
            (2, deque("MCD")),
            (3, deque("P")),
        ]

        self.assertEqual(
            expected,
            crane._initialise_stacks("test_input.txt"),
        )


if __name__ == "__main__":
    unittest.main()
