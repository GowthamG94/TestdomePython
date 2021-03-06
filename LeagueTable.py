# Created by Shawn O'Grady on 12/8/17.
# Copyright 2017 Shawn O'Grady. All rights reserved.

 #This code is a practice Python interview question from testdome.com

 #https://www.testdome.com/questions/python/league-table/11195?visibility=1&skillId=9

 # Problem statement: Implement the player_rank function that returns the player at the given rank
    #The LeagueTable class tracks the score of each player in a league. After each game, the player records their score with the record_result function.
    #The player's rank in the league is calculated using the following logic:
        #i) The player with the highest score is ranked first (rank 1). The player with the lowest score is ranked last.
        #ii) If two players are tied on score, then the player who has played the fewest games is ranked higher.
        #iii) If two players are tied on score and number of games played, then the player who was first in the list of players is ranked higher.
#Passes 3/3 tests

from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        #should return a player's name
        rankedPlayers={} #new dictionary w/ keys of player's rank and values of player's name
        i=1
        #fill out dictionary, initially sorted by order of player list
        for key in self.standings:
            rankedPlayers[i]=key
            i=i+1

        for key in self.standings:
            for j in rankedPlayers:
                #print(rankedPlayers)
                if(j<len(rankedPlayers)):
                    if self.standings[rankedPlayers[j+1]]['score']>self.standings[rankedPlayers[j]]['score']:
                        #swap
                        tmp=rankedPlayers[j]
                        rankedPlayers[j]=rankedPlayers[j+1]
                        rankedPlayers[j+1]=tmp
                    elif self.standings[rankedPlayers[j+1]]['score']==self.standings[rankedPlayers[j]]['score']:
                        #case where scores are tied
                        if self.standings[rankedPlayers[j+1]]['games_played']<self.standings[rankedPlayers[j]]['games_played']:
                            #swap
                            tmp=rankedPlayers[j]
                            rankedPlayers[j]=rankedPlayers[j+1]
                            rankedPlayers[j+1]=tmp

        return rankedPlayers[rank]

table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 2)
table.record_result('Chris', 3)
print(table.player_rank(1)) #Should show 'Arnold', ranking should be {1: 'Arnold', 2: 'Mike', 3: 'Chris'}
