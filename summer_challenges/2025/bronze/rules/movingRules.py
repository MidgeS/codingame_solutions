from rules.rulesBase import RulesBase
from agentCommand import AgentCommand
from agent import Agent
from turnValues import TurnValues

class MovingRules(RulesBase):

    def applyRules(self, agent_command: AgentCommand, agent: Agent, agents: dict[int,Agent], turn_values: TurnValues) -> bool:
        agent_command.setMoveTarget((8,8))
        return True