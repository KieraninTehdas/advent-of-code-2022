import sys

# A -> Rock, B -> Paper, C -> Scissors
# X -> Lose, Y -> Draw, Z -> Z

# Rock = 1, Paper = 2, Scissors = 3

# Win = 6, Draw = 3, Loss = 0


class Game:
    play_scores = {"A": 1, "B": 2, "C": 3}
    plays = ["A", "B", "C"]
    outcome_scores = {"X": 0, "Y": 3, "Z": 6}

    def __init__(self, rounds_input_filename):
        self.rounds_input_filename = rounds_input_filename

    def _calculate_your_play(self, opponent_play, round_outcome):
        winning_play = self.plays[
            (self.plays.index(opponent_play) + 1) % len(self.plays)
        ]
        losing_play = self.plays[
            (self.plays.index(opponent_play) - 1) % len(self.plays)
        ]

        if round_outcome == "X":
            return losing_play
        elif round_outcome == "Y":
            return opponent_play
        else:
            return winning_play

    def _calculate_round_score(self, opponent_play, round_outcome):
        your_play = self._calculate_your_play(opponent_play, round_outcome)

        return self.play_scores[your_play] + self.outcome_scores[round_outcome]

    def total_score(self):
        score = 0

        with open(self.rounds_input_filename, "r") as f:
            for round_ in f:
                plays = round_.strip().split(" ")
                score += self._calculate_round_score(plays[0], plays[1])

        return score


if __name__ == "__main__":
    print(Game(sys.argv[1]).total_score())
