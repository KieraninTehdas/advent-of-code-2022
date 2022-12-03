import sys

# A -> Rock, B -> Paper, C -> Scissors
# X -> Rock, Y -> Paper, Z -> Scissors

# Rock = 1, Paper = 2, Scissors = 3

# Win = 6, Draw = 3, Loss = 0


class Game:
    scores = {"A": 1, "B": 2, "C": 3}
    play_mappings = {"X": "A", "Y": "B", "Z": "C"}
    plays = ["A", "B", "C"]

    def __init__(self, rounds_input_filename):
        self.rounds_input_filename = rounds_input_filename

    def _calculate_round_score(self, opponent_play, your_play):
        play_score = self.scores[your_play]

        winning_play = self.plays[(self.plays.index(your_play) + 1) % len(self.plays)]
        losing_play = self.plays[(self.plays.index(your_play) - 1) % len(self.plays)]

        if opponent_play == winning_play:
            return play_score
        elif opponent_play == losing_play:
            return 6 + play_score
        else:
            return 3 + play_score

    def total_score(self):
        score = 0

        with open(self.rounds_input_filename, "r") as f:
            for round_ in f:
                plays = round_.strip().split(" ")
                score += self._calculate_round_score(
                    plays[0], self.play_mappings[plays[1]]
                )

        return score


if __name__ == "__main__":
    print(Game(sys.argv[1]).total_score())
