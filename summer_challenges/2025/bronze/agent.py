from typing import Self
from agentState import AgentState

class Agent:
    __id = 0
    __player_id = 0
    __current_cooldown = 0
    __shoot_cooldown = 0
    __optimal_range = 0
    __soaking_power = 0
    __splash_bombs = 0
    __wetness = 0
    __x = -1
    __y = -1
    __active = False
    __state: AgentState = AgentState.IDLE

    def __init__(self, agent_id, player, shoot_cooldown, optimal_range, soaking_power, splash_bombs, active):
        self.__id = agent_id
        self.__player_id = player
        self.__shoot_cooldown = shoot_cooldown
        self.__optimal_range = optimal_range
        self.__soaking_power = soaking_power
        self.__splash_bombs = splash_bombs
        self.__active = active

    def getAgentId(self) -> int:
        return self.__id
    
    def getPlayerId(self) -> int:
        return self.__player_id
    
    def getCurrentCooldown(self) -> int:
        return self.__current_cooldown
    
    def getShootCooldown(self) -> int:
        return self.__shoot_cooldown
    
    def getOptimalRange(self) -> int:
        return self.__optimal_range
    
    def getSoakingPower(self) -> int:
        return self.__soaking_power
    
    def getSplashBombs(self) -> int:
        return self.__splash_bombs
    
    def getWetness(self) -> int:
        return self.__wetness
    
    def getPosition(self) -> tuple[int,int]:
        return (self.__x, self.__y)
    
    def getActive(self) -> bool:
        return self.__active

    def updatePosition(self,x,y) -> Self:
        self.__x = x
        self.__y = y
        return self

    def updateCooldown(self, cooldown) -> Self:
        self.__current_cooldown = cooldown
        return self

    def updateSplashBombs(self,bombs) -> Self:
        self.__splash_bombs = bombs
        return self
    
    def updateWetness(self, wetness) -> Self:
        self.__wetness = wetness
        return self
    
    def getState(self) -> AgentState:
        return self.__state
    
    def setState(self, state: AgentState) -> Self:
        self.__state = state
        return self