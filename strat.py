from soccersimulator import Strategy
from soccersimulator import SoccerTeam, Simulation, SoccerAction
from toolbox import MyState, Action
from soccersimulator import Vector2D
from soccersimulator.settings import *

def fonceurball(mystate):
    return SoccerAction((mystate.ball_position-mystate.my_position)+(mystate.ball_vitesse)*7,Vector2D(0,0))
    
def fonceur(mystate):
    return SoccerAction((mystate.ball_position-mystate.my_position),mystate.position_but_adv-mystate.my_position)


def defonceur(mystate):
    action=Action(mystate)
    if(mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH//2):
        if(mystate.position_mon_but.x==GAME_WIDTH):
            return action.sprint(Vector2D(3*GAME_WIDTH//4,GAME_HEIGHT//2))
        else:
            return action.sprint(Vector2D(GAME_WIDTH//4,GAME_HEIGHT//2))

## Strategie
class ElLooser(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        return SoccerAction(Vector2D(0,0),mystate.position_but_adv)



class ElStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        return fonceur(mystate)
 


class ElDefenseur(Strategy):
    def __init__(self):
       Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        return defonceur(mystate)

