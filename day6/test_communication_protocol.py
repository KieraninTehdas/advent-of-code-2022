import unittest

from parameterized import parameterized

import communication_protocol


class TestCommunicationProtocol(unittest.TestCase):
    @parameterized.expand(
        [
            ["mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7],
            ["nppdvjthqldpwncqszvftbrmjlhg", 6],
            ["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10],
            ["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11],
        ]
    )
    def test_find_first_packet_marker_index(self, buffer, expected):
        self.assertEqual(
            communication_protocol.find_first_packet_marker_index(buffer), expected
        )


if __name__ == "__main__":
    unittest.main()
