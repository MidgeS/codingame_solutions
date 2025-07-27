from agent import Agent
from map import Map
from debugPrint import debugPrint
from agentStrategy import calculateAgentCommand
from turnValues import TurnValues


#region helper functions
def readAgentData(agent_data_count):
    global agents
    for i in range(agent_data_count):
        # agent_id: Unique identifier for this agent
        # player: Player id of this agent
        # shoot_cooldown: Number of turns between each of this agent's shots
        # optimal_range: Maximum manhattan distance for greatest damage output
        # soaking_power: Damage output within optimal conditions
        # splash_bombs: Number of splash bombs this can throw this game
        agent_id, player, shoot_cooldown, optimal_range, soaking_power, splash_bombs = [int(j) for j in input().split()]
        agents[agent_id] = Agent(agent_id, player, shoot_cooldown, optimal_range, soaking_power, splash_bombs, True)

def readActiveAgentData(agent_count):
    global agents
    global active_agents
    global own_active_agents
    global enemy_active_agents
    global my_id
    for i in range(agent_count):
        # cooldown: Number of turns before this agent can shoot
        # wetness: Damage (0-100) this agent has taken
        agent_id, x, y, cooldown, splash_bombs, wetness = [int(j) for j in input().split()]
        
        agents[agent_id].updatePosition(x,y)
        agents[agent_id].updateCooldown(cooldown)
        agents[agent_id].updateSplashBombs(splash_bombs)
        agents[agent_id].updateWetness(wetness)
        if(agents[agent_id].getPlayerId() == my_id):
            own_active_agents[agent_id] = agents[agent_id]
        else:
            enemy_active_agents[agent_id] = agents[agent_id]

        active_agents[agent_id] = agents[agent_id]
#endregion

#region game logic
agents : dict[int, Agent] = {}

my_id = int(input())  # Your player id (0 or 1)
agent_data_count = int(input())  # Total number of agents in the game

readAgentData(agent_data_count)

# width: Width of the game map
# height: Height of the game map
width, height = [int(i) for i in input().split()]
map = Map(width, height)

for i in range(height):
    inputs = input().split()
    for j in range(width):
        # x: X coordinate, 0 is left edge
        # y: Y coordinate, 0 is top edge
        x = int(inputs[3*j])
        y = int(inputs[3*j+1])
        tile_type = int(inputs[3*j+2])
        map.setCell(x,y,tile_type)

map.printMap()

areas = [(2, 2, False), (map.getWidth()-3, 2, False), (2, map.getHeight()-3, False), (map.getWidth()-3, map.getHeight()-3, False)]

agent_target = None
target_area = None

#region game loop
while True:
    agent_count = int(input())  # Total number of agents still in the game

    enemy_active_agents = {}
    own_active_agents = {}
    active_agents = {}
    
    readActiveAgentData(agent_count)

    my_agent_count = int(input())  # Number of alive agents controlled by you

    agent: Agent

    turn_values = TurnValues().calculateTurnValues(agents, map)

    for agent in own_active_agents.values():
        if agent.getPlayerId() == my_id:
            agent_command = calculateAgentCommand(agent, active_agents, map, turn_values)
            print(agent_command)
#endregion
#endregion