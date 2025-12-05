from StorageLayer.storageApi import DataAPI
from Models.Bracket import Bracket
from Models.Match import Match
from Models.Team import Team
import math
import random

class BracketGenerator:
    def __init__(self):
        self.__matchmodel=Match
    
        pass

    def playingames(self, teams):
        n=len(teams)
        rounds=0
        p = 1
        while p * 2 <= n:
            p *= 2
        extramatches = n - p

        teamcount_in_a_perfect_scenario_that_perfectly_fits_inside_a_bracket = n-extramatches # Do not shorten variable name !!! VERY IMPORTANT
        rounds=int(math.log2(teamcount_in_a_perfect_scenario_that_perfectly_fits_inside_a_bracket))

        return rounds, extramatches
    def generatebracket(self, teams: list[Team]):
        letterslol=['A','B','C','D','E','F','G']
        gamedata=self.playingames(teams)
        roundsplayed: dict ={}
        totalteams=len(teams)
        totalrounds=gamedata[0]
        extrarounds=gamedata[1]
        extrateams=[]
        isodd=1

        if extrarounds>0:
             teamsinround = (2**(totalrounds))/2
             isodd=2
        else:
             teamsinround = (2**(totalrounds))/2
        for i in range(1,isodd+1):
            if extrarounds>0:
                roundsplayed[(f'round{i}')]=[]
                
                for y in range(extrarounds):
                    team_A: Team = teams.pop(0)
                    team_B: Team = teams.pop(0)
                    matchid=f'{letterslol[random.randint(0,6)]}{random.randint(0,9)}' #note: matchid can have duplicates in this configuration, consider changing it
                    roundsplayed[(f'round{i}')].append((self.__matchmodel(matchid,team_A.teamName,team_B.teamName)))
                tempextrarounds=extrarounds
                extrarounds=0
                continue

            roundsplayed[f'round{i}'] = []

            for y in range(int(teamsinround-tempextrarounds)):    
                team_A = teams.pop(0)
                team_B = teams.pop(0)
                matchid=f'{letterslol[random.randint(0,6)]}{random.randint(0,9)}'
                roundsplayed[f'round{i}'].append(self.__matchmodel(matchid,team_A.teamName,team_B.teamName))

            for t in range(int(tempextrarounds)):
                team_A=teams.pop(0)
                team_B=f'{roundsplayed.get('round1')[t].team_A} or {roundsplayed.get('round1')[t].team_B}'
                matchid=f'{letterslol[random.randint(0,6)]}{random.randint(0,9)}'
                roundsplayed[f'round{i}'].append(self.__matchmodel(matchid,team_A.teamName,team_B))
        return roundsplayed
    
