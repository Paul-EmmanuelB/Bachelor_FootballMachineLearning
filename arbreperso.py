from soccersimulator import settings,SoccerTeam, Simulation, show_simu, KeyboardStrategy
from soccersimulator import Strategy, SoccerAction, Vector2D, load_jsonz,dump_jsonz,Vector2D
import logging
from arbre_utils import build_apprentissage,affiche_arbre,DTreeStrategy,apprend_arbre,genere_dot
from sklearn.tree 	import export_graphviz
from sklearn.tree import DecisionTreeClassifier

from strat import ElStrategy, ElDefenseur
import os.path
from arbre_decision import *
team2 = SoccerTeam("team2")
team2.add("Leonidas ", ElStrategy())
team2.add("Leonidus ", ElDefenseur())


def jouer_arbre(dt):
    ####
    # Utilisation de l'arbre
    ###
    dic = dict([(f.__name__,GenStrat(f)) for f in [dribble, se_positionner_haut,se_positionner_bas, donothing ,ralentir_moyen,shoot_but, up, down, left, right] ])
    treeStrat1 = DTreeStrategy(dt,dic,my_get_features)
    team3 = SoccerTeam("Arbre Team")
    team3.add("Joueur 1",treeStrat1)
    team3.add("Joueur 2",ElDefenseur())
    simu = Simulation(team2,team3)
    show_simu(simu)

if __name__=="__main__":
    fn = "test_states.jz"
    entrainement(fn)
    dt = apprentissage(fn)
    jouer_arbre(dt)

