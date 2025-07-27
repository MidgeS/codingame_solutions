from rules.rulesBase import RulesBase
from agentCommand import AgentCommand
from agent import Agent
from turnValues import TurnValues

class HunkerDownRules(RulesBase):

    def applyRules(agent_command: AgentCommand, agent: Agent, agents: dict[int,Agent], turn_values: TurnValues) -> bool:
        agent_command.setHunkerDown()
        return True