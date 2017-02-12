from soccersimulator import SoccerTeam, SoccerAction
from strat import ElStrategy, ElDefenseur, ElStrategySolo


## Creation d'une equipe
team1 = SoccerTeam(name="Liban",login="Harb")
team2 = SoccerTeam(name="France",login="PE")
team1.add("Hassan",ElStrategySolo())
team2.add("Paul",ElStrategy())
team2.add("Pogba",ElDefenseur())

def get_team(i):
    if i==1:
        return team1
    if i==2:
        return team2
    if i==4:
        return team4

