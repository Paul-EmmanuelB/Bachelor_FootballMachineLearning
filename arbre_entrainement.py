###### Attention, changer pour def , aller vers point de la ou va aller ballon et non donner l acceleration de ballon et joueuer!!!!



from soccersimulator import settings,SoccerTeam, Simulation, show_simu, KeyboardStrategy, SoccerAction
from soccersimulator import Strategy, SoccerAction, Vector2D, load_jsonz,dump_jsonz,Vector2D
import logging
from arbre_utils import build_apprentissage,affiche_arbre,DTreeStrategy,apprend_arbre,genere_dot
from sklearn.tree 	import export_graphviz
from sklearn.tree import DecisionTreeClassifier
import os.path


from strat import ElStrategy, ElDefenseur, ElLooser
from toolbox import MyState, Action, Shootameliorer
from soccersimulator import Strategy
from soccersimulator import SoccerAction
from soccersimulator import Vector2D
from soccersimulator.settings import *


## Strategie
 
def passe_pote(mystate):
    action=Action(mystate)
    if mystate.my_position.distance(mystate.ball_position)<1.65:
        return action.petit_shoot_joueur_proche
    return fonceurball(mystate)

def dribble(mystate):
    action=Action(mystate)
    if mystate.my_position.distance(mystate.ball_position)<1.65:
        return action.petit_shoot_but_adv
    return fonceurball(mystate)

def shoot_but(mystate):
    act=Action(mystate)
    x=mystate.ball_position.distance(mystate.position_but_adv)
    sh=Shootameliorer(mystate,x)
    if mystate.my_position.distance(mystate.ball_position)<1.65 and mystate.my_position.distance(mystate.position_but_adv)<GAME_WIDTH/2 :
        return sh.shoot
    if mystate.my_position.distance(mystate.ball_position)<1.65:
        return act.shoot_but_adv
    if mystate.my_position.distance(mystate.ball_position)<10:
        return SoccerAction(mystate.ball_position-mystate.my_position+(mystate.ball_vitesse),Vector2D())
    return fonceurball(mystate)


def fonceurball(mystate):
    return SoccerAction((mystate.ball_position-mystate.my_position)+(mystate.ball_vitesse)*10,Vector2D())
       
def donothing(mystate):
    return(SoccerAction(Vector2D(0,0),Vector2D(0,0)))


def se_positionner_bas(mystate):
        action=Action(mystate)
        if(mystate.position_mon_but.x==GAME_WIDTH):
            return action.sprint(Vector2D(0.7*GAME_WIDTH,mystate.ball_position.y))
        
            
        if(mystate.position_mon_but.x==0):
            return action.sprint(Vector2D(0.3*GAME_WIDTH,mystate.ball_position.y))


def se_positionner_haut(mystate):
        action=Action(mystate)
        if(mystate.position_mon_but.x==GAME_WIDTH):
                return action.sprint(Vector2D(0.35*GAME_WIDTH,mystate.ball_position.y))       
            
        if(mystate.position_mon_but.x==0):
                return action.sprint(Vector2D(0.65*GAME_WIDTH,mystate.ball_position.y))


def ralentir_moyen(mystate):
    return SoccerAction((mystate.ball_position-mystate.my_position).norm_max(0.05),Vector2D())


def godef(mystate):
    return SoccerAction((mystate.position_mon_but-mystate.my_position)+(mystate.ball_position-mystate.position_mon_but)/2,Vector2D())

def up(mystate):
    return SoccerAction(Vector2D(0,1).norm_max(0.1),Vector2D())

def down(mystate):
    return SoccerAction(Vector2D(0,-1).norm_max(0.1),Vector2D())

def left(mystate):
    return SoccerAction(Vector2D(-1,0).norm_max(0.1),Vector2D())

def right(mystate):
    return SoccerAction(Vector2D(1,0).norm_max(0.1),Vector2D())


#######
## Constructioon des equipes
#######

team1 = SoccerTeam("Equipe Active")
strat_j1 = KeyboardStrategy()
strat_j1.add('a',GenStrat(shoot_but))
strat_j1.add('z',GenStrat(dribble))
strat_j1.add('q',GenStrat(se_positionner_haut))
strat_j1.add('s',GenStrat(se_positionner_bas))
strat_j1.add('d',GenStrat(ralentir_moyen))
strat_j1.add('r',GenStrat(donothing))

strat_j1.add('o',GenStrat(up))
strat_j1.add('l',GenStrat(down))
strat_j1.add('k',GenStrat(left))
strat_j1.add('m',GenStrat(right))

team1.add("Jexp 1",strat_j1)
team1.add("Jexp 2",ElDefenseur())
team2 = SoccerTeam("team2")
team2.add("PPTI-14-303-10", ElStrategy())
team2.add("PPTI-14-303-09", ElDefenseur())



### Transformation d'un etat en features : state,idt,idp -> R^d
def my_get_features(state,idt,idp):
    """ extraction du vecteur de features d'un etat, ici distance a la balle, distance au but, distance balle but """
    p_pos= state.player_state(idt,idp).position
    f1 = p_pos.distance(state.ball.position)
    f2= p_pos.distance( Vector2D((2-idt)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)) #distance joueur -  but adv
    f3 = state.ball.position.distance(Vector2D((2-idt)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)) # distance ball - but adv
    return [f1,f2,f3]


def entrainement(fn):
    simu = Simulation(team1,team2)
    show_simu(simu)
    # recuperation de tous les etats
    training_states = strat_j1.states
    # sauvegarde dans un fichier
    dump_jsonz(training_states,fn)
