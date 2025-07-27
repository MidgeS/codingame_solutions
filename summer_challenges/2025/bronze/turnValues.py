from agent import Agent
from map import Map
from helper import calculateDistance
from debugPrint import debugPrint

class TurnValues():
    agent_distances = {}

    def calculateTurnValues(self, agents: dict[int,Agent], map: Map):
        self.__calculateAgentDistances(agents)
        return self

    def __calculateAgentDistances(self, agents: dict[int, Agent]):
        for x in range(1,len(agents)+1):
            for y in range(x,len(agents)+1):
                dist = calculateDistance(agents[x].getPosition(), agents[y].getPosition())
                self.agent_distances[(agents[x].getAgentId(),agents[y].getAgentId())] = dist
                self.agent_distances[(agents[y].getAgentId(),agents[x].getAgentId())] = dist
        return self
