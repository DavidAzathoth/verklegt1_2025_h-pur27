from Models.Team import Team
from Models.Tournament import Tournament
from Models.Match import Match

class Bracket:
    def __init__(self, teams: list[Team], tournamentname: Tournament, rounds: int): #tournamentname: tournament that this bracket is connected to
        self.teams = teams
        self.tournamentname = tournamentname
        self.rounds = rounds