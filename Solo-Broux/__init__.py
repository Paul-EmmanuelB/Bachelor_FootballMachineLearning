from strat import GolfStrat
from soccersimulator import SoccerTeam,show_simu
from soccersimulator import GolfState,Golf,Parcours1,Parcours2,Parcours3,Parcours4

GOLF = 0.001
SLALOM = 10.


team1 = SoccerTeam()
team2 = SoccerTeam()
team1.add("Player1",GolfStrat())
team2.add("Player2",GolfStrat())

def get_golf_team():
    return team1

def get_slalom_team():
    return team2

