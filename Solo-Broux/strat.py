from toolbox import MyState, Action
from soccersimulator import Strategy,SoccerAction,Vector2D
from soccersimulator.settings import *




def donothing():
    return(SoccerAction(Vector2D(0,0),Vector2D(0,0)))

class GolfStrat(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Golf")
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action=Action(mystate)
        x=mystate.ball_position.distance(Vector2D(GAME_WIDTH,GAME_HEIGHT/2)-mystate.my_position)
        zone=state.get_zones(mystate.my_team)
        if len(zone)==0:
            if mystate.my_position.distance(mystate.ball_position)<1.6:
                if mystate.my_position.distance(Vector2D(GAME_WIDTH,GAME_HEIGHT/2))<(1/.4)*GAME_WIDTH:
                    return SoccerAction(Vector2D(),(Vector2D(GAME_WIDTH,GAME_HEIGHT/2)-mystate.my_position).norm_max(1))
                return SoccerAction(Vector2D(),Vector2D(GAME_WIDTH,GAME_HEIGHT/2)-mystate.my_position)
            return SoccerAction(mystate.ball_position-mystate.my_position,Vector2D())
        z=zone[0]
        
        
        if mystate.ball_position.distance(z.position+z.l/2)<z.l/2:
            return donothing()
        if mystate.my_position.distance(mystate.ball_position)<1.6:
             if mystate.ball_position.distance(z.position+z.l/2)<2*z.l:
                 return SoccerAction(Vector2D(),(z.position+z.l/2-mystate.my_position).norm_max(0.05))
             return action.petit_shoot_zone(z.position+z.l/2)
        return SoccerAction(mystate.ball_position-mystate.my_position,Vector2D())



