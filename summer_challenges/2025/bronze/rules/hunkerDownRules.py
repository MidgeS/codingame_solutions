from rules.rulesBase import RulesBase
from agentCommand import AgentCommand
from agent import Agent
from map import Map
from turnValues import TurnValues

class HunkerDownRules(RulesBase):

    def applyRules(agent_command: AgentCommand, agent: Agent, agents: dict[int,Agent], map: Map, turn_values: TurnValues) -> bool:
        return False