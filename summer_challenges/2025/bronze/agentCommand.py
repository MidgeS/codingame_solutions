from typing import Self

class AgentCommand():
    __agent_id = -1
    __move_target = None
    __shoot_target = None
    __throw_target = None
    __hunker_down = False
    __message = None

    def __init__(self, agent_id: int):
        self.__agent_id = agent_id

    def __str__(self):
        return self.getOutputString()

    def __agent_string(self) -> str:
        return f"{self.__agent_id};"

    def setMoveTarget(self, target: tuple[int,int]) -> Self:
        self.__move_target = target
        return self

    def __move_string(self) -> str:
        return f"MOVE {self.__move_target[0]} {self.__move_target[1]};" if self.__move_target else ""

    def setShootTarget(self, target_id: int) -> Self:
        self.__shoot_target = target_id
        return self

    def __shoot_string(self) -> str:
        return f"SHOOT {self.__shoot_target};" if self.__shoot_target else ""

    def setThrowTarget(self, x: int, y: int) -> Self:
        self.__throw_target = (x,y)
        return self

    def __throw_string(self) -> str:
        return f"THROW {self.__throw_target[0]} {self.__throw_target[1]};" if self.__throw_target else ""

    def setHunkerDown(self) -> Self:
        self.__hunker_down = True
        return self

    def __hunker_down_string(self) -> str:
        return f"HUNKER_DOWN;" if self.__hunker_down else ""

    def setMessage(self, message: str) -> Self:
        self.__message = message
        return self

    def __message_string(self) -> str:
        return f"MESSAGE {self.__message};" if self.__message else ""
    
    def getOutputString(self) -> str:
        output = self.__agent_string()
        output += self.__move_string()
        output += self.__shoot_string()
        output += self.__throw_string()
        output += self.__hunker_down_string()
        output += self.__message_string()

        return output

