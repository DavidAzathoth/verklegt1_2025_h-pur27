from Models.Team import Team
from Models.Tournament import Tournament
from Models.Match import Match

class Bracket:
    def __init__(self, tournamentname: str, rounds: dict[list]): #tournamentname: tournament that this bracket is connected to
        self.tournamentname = tournamentname
        self.rounds: dict[list] = rounds
    def createCSVDict(self)-> dict:
        """Creates a dictionary to store in a csv file"""
        ret_dic={'tournamentname':self.tournamentname,'rounds':self.rounds}
        return ret_dic

