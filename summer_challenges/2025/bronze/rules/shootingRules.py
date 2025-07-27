from rules.rulesBase import RulesBase
from agentCommand import AgentCommand
from agent import Agent
from turnValues import TurnValues

class ShootingRules(RulesBase):

    def applyRules(agent_command: AgentCommand, agent: Agent, agents: dict[int,Agent], turn_values: TurnValues) -> bool:
        agent_command.setShootTarget(4)
        return True