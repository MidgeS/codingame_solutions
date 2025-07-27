from agent import Agent
from agentState import AgentState
from agentCommand import AgentCommand
from debugPrint import debugPrint
from turnValues import TurnValues
from rules.rulesFactory import RuleType, getRulesHandler

moving_rules = getRulesHandler(RuleType.MOVING)
shooting_rules = getRulesHandler(RuleType.SHOOTING)
throwing_rules = getRulesHandler(RuleType.THROWING)
hunker_down_rules = getRulesHandler(RuleType.HUNKER_DOWN)

def calculateAgentCommand(agent: Agent, agents: dict[int,Agent], turn_values: TurnValues) -> AgentCommand:
    agent_command = AgentCommand(agent.getAgentId())
    ApplyMovingRules(agent_command, agent, agents, turn_values)
    ApplyCombatRules(agent_command, agent, agents, turn_values)

    return agent_command
        
def ApplyMovingRules(agent_command: AgentCommand, agent: Agent, agents: dict[int,Agent], turn_values: TurnValues):
    moving_rules.applyRules(agent_command, agent, agents, turn_values)
    pass

def ApplyCombatRules(agent_command: AgentCommand, agent: Agent, agents: dict[int,Agent], turn_values: TurnValues):
    hunker_down = ApplyHunkerDownRules(agent_command, agent, agents, turn_values)
    if not hunker_down:
        throw_bomb = ApplyThrowRules(agent_command, agent, agents, turn_values)
        if not throw_bomb:
            ApplyShootingRules(agent_command, agent, agents, turn_values)

def ApplyHunkerDownRules(agent_command: AgentCommand, agent: Agent, agents: dict[int,Agent], turn_values: TurnValues) -> bool:
    return hunker_down_rules.applyRules(agent_command, agent, agents, turn_values)

def ApplyThrowRules(agent_command: AgentCommand, agent: Agent, agents: dict[int,Agent], turn_values: TurnValues) -> bool:
    return throwing_rules.applyRules(agent_command, agent, agents, turn_values)

def ApplyShootingRules(agent_command: AgentCommand, agent: Agent, agents: dict[int,Agent], turn_values: TurnValues) -> bool:
    return shooting_rules.applyRules(agent_command, agent, agents, turn_values)

## plan
# for each agent
    # calculate enemies in shootig range
        # calculate cover to that enemy
    # calculate which enemies can hit him
        # calculate cover to that enemy
    # calculate which enemy can throw bomb hitting
# 
    # find covers in range to closest enemy
    # find enemy groups for bombing
# 
    # prevent grouping to reduce enemy bomb efficiency
# 
# agents should have combat states
    # - moving
    # - combat
    # - defence
    # - flee
# 
# 
# state:
    # moving:
        # enemy in range?
            # enter combat state
        # : apply movement rule
    # combat:
        

