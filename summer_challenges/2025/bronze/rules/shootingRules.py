from rules.rulesBase import RulesBase
from agentCommand import AgentCommand
from agent import Agent
from map import Map
from turnValues import TurnValues
from helper import calculateDistance

class ShootingRules(RulesBase):

    def applyRules(agent_command: AgentCommand, agent: Agent, agents: dict[int,Agent], map: Map, turn_values: TurnValues) -> bool:
        
        shoot_target = -1

        most_damage_after_hit = 0
        for x in agents:
            if agents[x].getPlayerId() != agent.getPlayerId():
                dist = calculateDistance(agent.getPosition(), agents[x].getPosition())
                damage = 0
                is_in_optimal = False
                is_in_double = False
                if dist <= agent.getOptimalRange():
                    is_in_optimal = True
                    damage = agent.getSoakingPower()
                elif dist <= agent.getOptimalRange() * 2:
                    is_in_double = True
                    damage = agent.getSoakingPower() / 2
                
                #if target gets killed look no further
                damage_after_hit = agents[x].getWetness() + damage
                if damage_after_hit >= 100:
                    shoot_target = x
                    break

                if is_in_optimal and damage_after_hit > most_damage_after_hit:
                    shoot_target = x
                    most_damage_after_hit = damage_after_hit

                if is_in_double and dist - agent.getCurrentCooldown() <= agent.getOptimalRange():
                    continue
                else:
                    if damage_after_hit > most_damage_after_hit:
                        shoot_target = x
                        most_damage_after_hit = damage_after_hit

        if shoot_target != -1:
            agent_command.setShootTarget(shoot_target)
            return True
        
        return False
    

    

        in_cooldown_range = []
        in_optimal_range = []

        for x in agents:
            if agents[x].getPlayerId() != agent.getPlayerId():
                dist = calculateDistance(agent.getPosition(), agents[x].getPosition())
                if dist < agent.getOptimalRange() + 1:
                    in_optimal_range.append(x)
                elif dist < agent.getOptimalRange() + agent.getCurrentCooldown(): #include cooldown
                    in_cooldown_range.append(x)

        for optimal_enemy in in_optimal_range:
            shoot_target = optimal_enemy #tempory pick first
            #optimizations
                #pick target by, enemy wetness, shooter power, enemy distance, enemy power, shooter wetness 

        if shoot_target == -1:
            for cooldown_enemy in in_cooldown_range:
                shoot_target = cooldown_enemy #tempory pick first
                #optimizations
                    #pick target by, enemy wetness, shooter power, enemy distance, enemy power, shooter wetness
        