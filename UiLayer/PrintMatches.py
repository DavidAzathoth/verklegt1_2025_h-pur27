from Models.Tournament import Tournament
from Models.Bracket import Bracket
from Models.Match import Match

class PrintMatches:
    def __init__(self, tournament: Tournament):
        self.tournament = tournament


    def print_results_table(self):
        bracket: Bracket = self.tournament.bracket

        max_team = 0
        max_string = 0

        # Find the longest team name for spacing, and maximum line length of a match for dot lines
        for i, matches in bracket.rounds.items(): 
            for match in matches:
                match: Match
            
                current_team = max(len(match.team_A), len(match.team_B))
                current_string = len(f"- Match {match.matchID:<4}: {match.team_A:<{max_team + 2}} vs   {match.team_B:<{max_team + 2}} (winner: {match.matchWinner})")

                if current_team > max_team:
                    max_team = current_team

                if current_string > max_string:
                    max_string = current_string

        rounds = bracket.rounds.items()
        total_rounds = len(rounds)

        names = {total_rounds - 3: "Quarterfinals", total_rounds -2: "Semifinals", total_rounds -1: "Finals"}

        for index, (round_number, matches) in enumerate(rounds):
            
            if index in names:
                round_name = names[index]
            else:
                round_name = f"Round {round_number}"

            print(f"{round_name}: ")
            print("-" * max_string)
            print()

            for match in matches:
                print(f"- Match {match.matchID:<4}: {match.team_A:<{max_team + 2}} vs   {match.team_B:<{max_team + 2}} (winner: {match.matchWinner})")    
            print()
            print("-" * max_string)
            print()


    def print_schedule_table(self):
        bracket: Bracket = self.tournament.bracket
        
        max_team = 0
        max_string = 0
        # Find the longest team name for spacing, and maximum line length of a match for dot lines
        for i, matches in bracket.rounds.items(): 
            for match in matches:
                match: Match

                current_team = max(len(match.team_A), len(match.team_B))
                current_string = len(f"- Match {match.matchID:<4}: {match.team_A:<{max_team + 2}} vs   {match.team_B:<{max_team + 2}} Date: {match.matchDate},  {match.matchTime}")

                if current_team > max_team:
                    max_team = current_team

                if current_string > max_string:
                    max_string = current_string

        # Print schedule table loop
        for i, matches in bracket.rounds.items():
            
            print(f"Round {i}:")
            print("-" * max_string)
            print()
                
            for match in matches:
                print(f"- Match {match.matchID:<4}: {match.team_A:<{max_team + 2}} vs   {match.team_B:<{max_team + 2}} Date: {match.matchDate},  {match.matchTime}")    
            print()
            print("-" * max_string)
