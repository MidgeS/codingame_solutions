from rules.rulesBase import RulesBase
from agentCommand import AgentCommand
from agent import Agent
from map import Map
from turnValues import TurnValues
from helper import clampValues
from debugPrint import debugPrint

class ThrowingRules(RulesBase):

    def applyRules(agent_command: AgentCommand, agent: Agent, agents: dict[int,Agent], map: Map, turn_values: TurnValues) -> bool:

        x_min = clampValues(agent.getPosition()[0] - 4, 0, map.getWidth())
        x_max = clampValues(agent.getPosition()[0] + 4, 0, map.getWidth())
        y_min = clampValues(agent.getPosition()[1] - 4, 0, map.getHeight())
        y_max = clampValues(agent.getPosition()[1] + 4, 0, map.getHeight())

        
        if agent.getAgentId() == 1:
            debugPrint(f"{x_min} {x_max} {y_min} {y_max}")

        bomb_target = (-1,-1)
        best_target_count = 0
        for x in range(x_min, x_max):
            for y in range(y_min, y_max):
                if agent.getAgentId() == 1:
                    debugPrint(f"check target {x}, {y}")
                possible_targets = 0
                #calculate enemies in explosion zone AND dont hit own agents
                x_min_explosion = clampValues(x - 1, 0, map.getWidth())
                x_max_explosion = clampValues(x + 1, 0, map.getWidth())
                y_min_explosion = clampValues(y - 1, 0, map.getHeight())
                y_max_explosion = clampValues(y + 1, 0, map.getHeight())

                for a in agents:
                    if (x_min_explosion <= agents[a].getPosition()[0] <= x_max_explosion and
                        y_min_explosion <= agents[a].getPosition()[1] <= y_max_explosion):
                        if agents[a].getPlayerId() == agent.getPlayerId():
                            debugPrint("would hit own agent")
                            break
                        else:
                            possible_targets += 1
                            debugPrint(f"new target count {possible_targets}")
                else:
                    if agent.getAgentId() == 1:
                        debugPrint("finished without breaking")
                    if possible_targets > 1 and possible_targets > best_target_count:
                        best_target_count = possible_targets
                        bomb_target = (x,y)
                        debugPrint(f"new target {bomb_target}")

        debugPrint(f"agent {agent.getAgentId()} target {bomb_target} hits {best_target_count}")
        if bomb_target[0] > -1 and bomb_target[1] > -1 and agent.getSplashBombs() > 0:
            agent_command.setThrowTarget(bomb_target)
            return True
        
        return False