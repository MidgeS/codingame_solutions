from enum import Enum

class AgentState(Enum):
    IDLE = 0
    MOVING = 1
    COMBAT = 2
    DEFENCE = 3
    FLEE = 4