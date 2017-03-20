from soccersimulator import Strategy, SoccerTeam,SoccerAction
from toolbox import MyState, Action, Shootameliorer
from soccersimulator import Vector2D
from soccersimulator.settings import *

from soccersimulator import SimuGUI,show_state,show_simu, Simulation
from strat import ElDefenseur, ElStrategy, ElLooser, ElStrategySolo, donothing, fonceurball

def shoot_but(mystate):
    act=Action(mystate)
    x=mystate.ball_position.distance(mystate.position_but_adv)
    sh=Shootameliorer(mystate,x)
    if mystate.my_position.distance(mystate.ball_position)<1.65 and mystate.my_position.distance(mystate.position_but_adv)<GAME_WIDTH/2 :
        return sh.shoot
    if mystate.my_position.distance(mystate.ball_position)<1.65:
        return act.shoot_but_adv
    return fonceurball(mystate)
        
        
class ElStrategySoloAm(Strategy):
   def __init__(self):
       Strategy.__init__(self,"ElMatadorSolo")
       self.mydic = dict()
       self.mydic["c"] = 0
   def compute_strategy(self,state,id_team,id_player):
       mystate= MyState(state,id_team,id_player)
       self.mydic["c"]+=1
       return shoot_but(mystate)

        
        
        
        
        
## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("Paul",ElStrategySolo())
team2.add("Booba",ElStrategySoloAm())





#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)