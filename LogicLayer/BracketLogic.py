from Models.Bracket import Bracket
from Models.Match import Match

class BracketLogic:

    def __init__(self):
        pass

    
    def getnamedrounds(self, bracket):

        round_keys = sorted(bracket.rounds.keys(), key = int)
        total_rounds = len(round_keys)

        names = {}

        for round_key in round_keys:
            index = int(round_key)
            rounds_left = total_rounds - index

            if rounds_left == 0:
                label = "Final"
            elif rounds_left == 1:
                label = "Semifinals"
            elif rounds_left == 2:
                label = "Quarterfinals"
            else:
                label = f"Round {index}"
            
            names[round_key] = label

        return names        