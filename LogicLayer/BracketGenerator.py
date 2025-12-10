from StorageLayer.storageApi import DataAPI
from Models.Bracket import Bracket
from Models.Match import Match
from Models.Team import Team
from Models.Tournament import Tournament
import math
import random
from datetime import date, time, timedelta, datetime
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
        #days=(enddate-startdate).days

        ##Stringify dates
        #startdate=startdate.strftime("%d/%m/%Y")
        #enddate=enddate.strftime("%d/%m/%Y")


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


        if extrarounds>0:
             teamsinround = (2**(totalrounds))/2
             totalrounds+=1
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
            p=0
            for k in range(0,int(tempextrarounds-teamsinround)):
                team_A=f'{roundsplayed.get('1')[p].team_A} or {roundsplayed.get('1')[p].team_B}'
                p+=1
                team_B=f'{roundsplayed.get('1')[p].team_A} or {roundsplayed.get('1')[p].team_B}'
                p+=1
                while True:
                    matchid=f'M{len(existingmatches)+num}' #note: matchid can have duplicates in this configuration, consider changing it
                    if matchid not in existingmatchids:
                        num+=1
                        break
                    else:
                        num+=1
                roundsplayed[f'{i}'].append(self.__matchmodel(matchid,team_A,team_B))

            if tempextrarounds>=8:
                prelim = int(teamsinround-(tempextrarounds-teamsinround))
            else:
                prelim = int(tempextrarounds)
            for t in range(p, prelim+p):
                '''If this returns pop from empty string error then the amount of teams is under 16 validate before generating bracket'''
                team_A = teams[teamnum]
                teamnum+=1
                team_B=f'{roundsplayed.get('1')[t].team_A} or {roundsplayed.get('1')[t].team_B}'
                while True:
                        matchid=f'M{len(existingmatches)+num}' #note: matchid can have duplicates in this configuration, consider changing it
                        if matchid not in existingmatchids:
                            num+=1
                            break
                        else:
                            num+=1
                roundsplayed[f'{i}'].append(self.__matchmodel(matchid,team_A.teamName,team_B))
        
        for i in range(len(roundsplayed)+1,totalrounds+1):
            teamsinround=teamsinround/2
            roundsplayed[(f'{i}')]=[]
            for z in range(int(teamsinround)):
                while True:
                    matchid=f'M{len(existingmatches)+num}' #note: matchid can have duplicates in this configuration, consider changing it
                    if matchid not in existingmatchids:
                        num+=1
                        break
                    else:
                        num+=1
                roundsplayed[f'{i}'].append(self.__matchmodel(matchid,'TBD','TBD'))


        #Save all matches before returning
        slots = self.generate_slots_full_range(startdate,enddate,servers=1,match_minutes=60)

        used = self.schedule_round_blocks(roundsplayed, slots, servers=1)

        total_games = len(tournament.teams) - 1

        generated = sum(len(v) for v in roundsplayed.values())
        remaining = total_games - generated
        self.schedule_spread_in_round_order(roundsplayed, slots)
        #tbd_idxs = self.spread_indices(used, len(slots)-1,remaining)
        #tbd_slots= [slots[i] for i in tbd_idxs]

        

        for round in roundsplayed.keys():
            for match in roundsplayed.get(round):
               self.__dataapi.saveMatch(match.createCSVDict())

        bracket=Bracket(tournament.name,roundsplayed)
        tournament.bracket=bracket
        return
    
    def updateBracket(self, bracket):
        pass


    def generate_slots_full_range(self, start: date, end: date, servers: int,
                                  match_minutes=60, buffer_minutes=0,
                                  day_start=time(10,0), day_end=time(16,0)):
        L = match_minutes + buffer_minutes
        start_min = day_start.hour*60 + day_start.minute
        end_min   = day_end.hour*60 + day_end.minute
        W = end_min - start_min

        rows_per_day  = W // L               # 60min -> 6
        slots_per_day = servers * rows_per_day
        days = (end - start).days + 1        # inclusive
        capacity = days * slots_per_day

        slots = []
        for g in range(capacity):
            day_idx, r = divmod(g, slots_per_day)
            server, row = divmod(r, rows_per_day)
            mins = start_min + row * L
            hh, mm = divmod(mins, 60)
            d = start + timedelta(days=day_idx)
            slots.append((d, time(hh, mm), server))
        return slots

    def schedule_round_blocks(self,roundsplayed: dict, slots, servers: int):
        def align_to_next_row(i):
            return ((i + servers - 1) // servers) * servers

        used = 0
        for r in sorted(roundsplayed.keys(), key=lambda x: int(x)):
            used = align_to_next_row(used)
            for m in roundsplayed[r]:
                d, t, s = slots[used]
                m.matchDate = d.strftime("%d/%m/%Y")
                m.matchTime = t.strftime("%H:%M")
                m.server = s
                used += 1
            used = align_to_next_row(used)
        return used  # index of next free slot

    def spread_indices(self, start_g: int, end_g: int, k: int):
        if k <= 0: return []
        if k == 1: return [end_g]
        span = end_g - start_g
        return [start_g + (j * span) // (k - 1) for j in range(k)]

    def schedule_spread_in_round_order(self, roundsplayed: dict, slots):
        # Flatten matches in round order
        matches = []
        for r in sorted(roundsplayed.keys(), key=lambda x: int(x)):
            matches.extend(roundsplayed[r])

        if len(matches) == 0:
            return

        idxs = self.spread_indices(0, len(slots) - 1, len(matches))

        for m, idx in zip(matches, idxs):
            d, t, s = slots[idx]
            m.matchDate = d.strftime("%d/%m/%Y")
            m.matchTime = t.strftime("%H:%M")
            m.server = s





































    # def _generate_slots(self,start: date, end: date, servers: int,
    #                     match_minutes=40, buffer_minutes=0,
    #                     day_start=time(10,0), day_end=time(16,0),
    #                     count: int | None = None):
    #     L = match_minutes + buffer_minutes
    #     start_min = day_start.hour*60 + day_start.minute
    #     end_min   = day_end.hour*60 + day_end.minute
    #     W = end_min - start_min

    #     rows_per_day = W // L                 # 40min -> 9 rows/day (10:00..15:20)
    #     slots_per_day = servers * rows_per_day
    #     days = (end - start).days + 1         # inclusive
    #     capacity = days * slots_per_day

    #     if count is None:
    #         count = capacity
    #     if count > capacity:
    #         raise ValueError(f"Not enough capacity: need {count}, have {capacity} slots.")

    #     slots = []
    #     for g in range(count):  # row-major: server changes fastest inside each time row
    #         day_idx, r = divmod(g, slots_per_day)
    #         server, row = divmod(r, rows_per_day)
    #         mins = start_min + row * L
    #         hh, mm = divmod(mins, 60)
    #         d = start + timedelta(days=day_idx)
    #         slots.append((d, time(hh, mm), server))
    #     return slots, rows_per_day

    # def schedule_generated_and_tbd(self,roundsplayed: dict, start: date, end: date, servers: int, team_count: int,
    #                                match_minutes=40, buffer_minutes=0,
    #                                day_start=time(10,0), day_end=time(16,0)):
    #     total_games = team_count - 1
    #     slots, _ = self._generate_slots(start, end, servers, match_minutes, buffer_minutes, day_start, day_end, count=total_games)

    #     def align_to_next_row(i):
    #         return ((i + servers - 1) // servers) * servers

    #     # 1) Schedule the generated rounds in order, in blocks
    #     used_until = 0
    #     for r in sorted(roundsplayed.keys(), key=lambda x: int(x)):
    #         matches = roundsplayed[r]
    #         used_until = align_to_next_row(used_until)

    #         for m in matches:
    #             d, t, s = slots[used_until]
    #             m.matchDate = d.strftime("%d/%m/%Y")
    #             m.matchTime = t.strftime("%H:%M")
    #             m.server = s
    #             used_until += 1

    #         used_until = align_to_next_row(used_until)

    #     # 2) Reserve remaining as TBD, SPREAD OUT until the last slot
    #     remaining = total_games - sum(len(v) for v in roundsplayed.values())
    #     if remaining <= 0:
    #         return []  # no TBD needed

    #     start_g = used_until
    #     end_g = total_games - 1  # force final to be last slot of the range

    #     # If we already passed end_g (shouldn’t happen), just return none
    #     if start_g > end_g:
    #         return []

    #     if remaining == 1:
    #         indices = [end_g]
    #     else:
    #         span = end_g - start_g
    #         indices = [start_g + (j * span) // (remaining - 1) for j in range(remaining)]

    #     tbd_slots = [slots[g] for g in indices]
    #     return tbd_slots

