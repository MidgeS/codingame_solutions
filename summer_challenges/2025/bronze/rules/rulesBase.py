from agentCommand import AgentCommand
from agent import Agent
from map import Map
from turnValues import TurnValues
from abc import ABC, abstractmethod

class RulesBase(ABC):

    @abstractmethod
    def applyRules(self, agent_command: AgentCommand, agent: Agent, agents: dict[int,Agent], map: Map, turn_values: TurnValues) -> bool:
        pass