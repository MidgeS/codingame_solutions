from rules.rulesBase import RulesBase
from agentCommand import AgentCommand
from agent import Agent
from map import Map
from turnValues import TurnValues
from helper import calculateDistance, clampValues
from debugPrint import debugPrint

class MovingRules(RulesBase):

    def applyRules(self, agent_command: AgentCommand, agent: Agent, agents: dict[int,Agent], map: Map, turn_values: TurnValues) -> bool:

        #in optimal range of enemy
            #move away from enemy
        #in double range of enemy
            #move to nearest cover to that enemy
        #free range
            #move to closest enemy

        #find all enemys for which we are in shooting range
        in_double_range = []
        in_optimal_range = []
        closest_distance = 200
        closest_index = -1

        #debugPrint(f"agend: {agent.getAgentId()}")

        for x in agents:
            if agents[x].getPlayerId() != agent.getPlayerId():
                distance = calculateDistance(agent.getPosition(), agents[x].getPosition())

                if distance < closest_distance:
                    closest_index = x

                if distance <= agents[x].getOptimalRange():
                    #debugPrint(f"in optimal range of {x} distance {distance}")
                    in_optimal_range.append(x)
                elif distance <= agents[x].getOptimalRange() * 2:
                    #debugPrint(f"in double range of {x} distance {distance}")
                    in_double_range.append(x)

        #first check if any optimal range and if so move away from strongest
        strongest_power = 0
        strongest_index = -1
        for optimal_enemy in in_optimal_range:
            if agents[optimal_enemy].getSoakingPower() > strongest_power:
                strongest_index = optimal_enemy
        if strongest_index > -1:
            #debugPrint(f"flee from {strongest_index}")
            enemy_position = agents[strongest_index].getPosition()
            agent_position = agent.getPosition()
            enemy_direction = (enemy_position[0] - agent_position[0], enemy_position[0] - agent_position[0])
            move_target = (clampValues(agent_position[0] - enemy_direction[0], 0, map.getWidth()), clampValues(agent_position[1] - enemy_direction[1], 0, map.getHeight()))
            agent_command.setMoveTarget(enemy_position) #move to enemy since fleeing was stupid till now
            return True

        strongest_power = 0
        strongest_index = -1
        for double_enemy in in_double_range:
            if agents[double_enemy].getSoakingPower() > strongest_power:
                strongest_index = double_enemy
        if strongest_index > -1:
            #TODO find nearest cover and return
            agent_command.setMoveTarget(agent.getPosition())
            return True

        if closest_distance > agent.getOptimalRange():
            agent_command.setMoveTarget(agents[closest_index].getPosition())

        return True