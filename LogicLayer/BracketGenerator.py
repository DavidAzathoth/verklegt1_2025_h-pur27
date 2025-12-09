from StorageLayer.storageApi import DataAPI
from Models.Bracket import Bracket
from Models.Match import Match
from Models.Team import Team
from Models.Tournament import Tournament
import math
import random
from datetime import datetime, date
class BracketGenerator:
    def __init__(self):
        self.__matchmodel=Match
        self.__dataapi=DataAPI()
    
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
    
    def generatebracket(self, tournament: Tournament):
        """Generate inital bracket for tournament, accounting for a non base 2 number of teams(16,32,64...)"""
        teams = tournament.teams
        startdate = date(*(list(map(int,(reversed(tournament.startDate.split('/')))))))
        enddate = date(*(list(map(int,(reversed(tournament.endDate.split('/')))))))

        #Calculate days that the tournament will be held
        days=(enddate-startdate).days

        #Stringify dates
        startdate=startdate.strftime("%d/%m/%Y")
        enddate=enddate.strftime("%d/%m/%Y")


        existingmatches=self.__dataapi.loadMatches()
        existingmatchids=[x.get('matchID') for x in existingmatches]
        num=1
        gamedata=self.playingames(teams)
        totalrounds2 = (len(tournament.teams)-1)
        roundsplayed: dict ={}
        totalrounds=gamedata[0]
        extrarounds=gamedata[1]
        tempextrarounds=0
        isodd=1
        teamnum=0

        matchschedule={}
        for day in range(1,days):
            pass
        while totalrounds2>1:
            pass

        if extrarounds>0:
             teamsinround = (2**(totalrounds))/2
             isodd=2
        else:
             teamsinround = (2**(totalrounds))/2
        for i in range(1,isodd+1):
            if extrarounds>0:
                roundsplayed[(f'{i}')]=[]
                
                for x in range(extrarounds):
                    team_A: Team = teams[teamnum]
                    teamnum+=1
                    team_B: Team = teams[teamnum]
                    teamnum+=1
                    while True:
                        matchid=f'M{len(existingmatches)+num}' #note: matchid can have duplicates in this configuration, consider changing it
                        if matchid not in existingmatchids:
                            num+=1
                            break
                        else:
                             num+=1
                    roundsplayed[(f'{i}')].append((self.__matchmodel(matchid,team_A.teamName,team_B.teamName)))
                tempextrarounds=extrarounds
                extrarounds=0
                continue

            roundsplayed[f'{i}'] = []

            for y in range(int(teamsinround-tempextrarounds)):   
                team_A = teams[teamnum]
                teamnum+=1
                team_B = teams[teamnum]
                teamnum+=1
                while True:
                    matchid=f'M{len(existingmatches)+num}' #note: matchid can have duplicates in this configuration, consider changing it
                    if matchid not in existingmatchids:
                        num+=1
                        break
                    else:
                        num+=1
                roundsplayed[f'{i}'].append(self.__matchmodel(matchid,team_A.teamName,team_B.teamName))

            for t in range(int(tempextrarounds)):
                '''If this returns pop from empty string error then the amount of teams is under 16 validate before generating bracket'''
                teamnum+=1
                team_A=[teamnum]
                team_B=f'{roundsplayed.get('1')[t].team_A} or {roundsplayed.get('1')[t].team_B}'
                while True:
                        matchid=f'M{len(existingmatches)+num}' #note: matchid can have duplicates in this configuration, consider changing it
                        if matchid not in existingmatchids:
                            num+=1
                            break
                        else:
                            num+=1
                roundsplayed[f'{i}'].append(self.__matchmodel(matchid,team_A.teamName,team_B))
        #Save all matches before returning
        for round in roundsplayed.keys():
            for match in roundsplayed.get(round):
               self.__dataapi.saveMatch(match.createCSVDict())
        bracket=Bracket(tournament.name,roundsplayed)
        tournament.bracket=bracket
        return
    def updateBracket(self, bracket):
        pass
