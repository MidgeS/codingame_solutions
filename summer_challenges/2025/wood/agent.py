import sys
import math

#region definitions
class Agent:
    id = 0
    player_id = 0
    shoot_cooldown = 0
    optimal_range = 0
    soaking_power = 0
    splash_bombs = 0
    wetness = 0
    pos_x = -1
    pos_y = -1
    active = False

    def __init__(self, agent_id, player, shoot_cooldown, optimal_range, soaking_power, splash_bombs, active):
        self.id = agent_id
        self.player_id = player
        self.shoot_cooldown = shoot_cooldown
        self.optimal_range = optimal_range
        self.soaking_power = soaking_power
        self.splash_bombs = splash_bombs
        self.active = active

    def updatePosition(self,x,y):
        self.x = x
        self.y = y

    def updateCooldown(self, cooldown):
        self.shoot_cooldown = cooldown

    def updateSplashBombs(self,bombs):
        self.splash_bombs = bombs
    
    def updateWetness(self, wetness):
        self.wetness = wetness

def findClosestAgent(target, agents):
    closest_agent = 0
    closest_distance = 2000 #find better upper limit

    for agent in agents.values():
        agent_dist = calculateDistance(target, (agent.x, agent.y))
        if agent_dist < closest_distance:
            closest_agent = agent.id
            closest_distance = agent_dist

    return closest_agent

def findClosestTarget(agent, targets):
    closest_target = 0
    closest_distance = 2000 #find better upper limit

    for target in targets:
        target_dist = calculateDistance((agent.x, agent.y), target)
        if target_dist < closest_distance:
            closest_target = target
            closest_distance = target_dist
    
    return closest_target

# first step simple manhatten distance ignoring obstacles
def calculateDistance(position, target):
    dist_x = abs(target[0] - position[0])
    dist_y = abs(target[1] - position[1])
    dist = dist_x + dist_y
    return dist

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
    global own_active_agents
    global enemy_active_agents
    for i in range(agent_count):
        # cooldown: Number of turns before this agent can shoot
        # wetness: Damage (0-100) this agent has taken
        agent_id, x, y, cooldown, splash_bombs, wetness = [int(j) for j in input().split()]
        
        agents[agent_id].updatePosition(x,y)
        agents[agent_id].updateCooldown(cooldown)
        agents[agent_id].updateSplashBombs(splash_bombs)
        agents[agent_id].updateWetness(wetness)
        if(agents[agent_id].player_id == 0):
            own_active_agents[agent_id] = agents[agent_id]
        else:
            enemy_active_agents[agent_id] = agents[agent_id]
#endregion

#region game logic
agents = {}

my_id = int(input())  # Your player id (0 or 1)
agent_data_count = int(input())  # Total number of agents in the game

readAgentData(agent_data_count)

# width: Width of the game map
# height: Height of the game map
width, height = [int(i) for i in input().split()]
for i in range(height):
    inputs = input().split()
    for j in range(width):
        # x: X coordinate, 0 is left edge
        # y: Y coordinate, 0 is top edge
        x = int(inputs[3*j])
        y = int(inputs[3*j+1])
        tile_type = int(inputs[3*j+2])

#region game loop
while True:
    agent_count = int(input())  # Total number of agents still in the game

    enemy_active_agents = {}
    own_active_agents = {}
    
    readActiveAgentData(agent_count)

    my_agent_count = int(input())  # Number of alive agents controlled by you
    
    print(f"agents: {my_agent_count}", file=sys.stderr, flush=True)

    #closest_a = findClosestAgent((6,1),own_active_agents)
    #print(f"closest to a: {closest_a}", file=sys.stderr, flush=True)

    #closest_b = findClosestAgent((6,3),own_active_agents)
    #print(f"closest to b: {closest_b}", file=sys.stderr, flush=True)

    targets = [(6,1), (6,3)]
    for agent in own_active_agents.values():
        if agent.player_id == 0:
            target = findClosestTarget(agent, targets)
            print(f"agent: {agent.id} -> target: {target}", file=sys.stderr, flush=True)
            print(f"{agent.id};MOVE {target[0]} {target[1]}")
    # for agent in enemy_active_agents.values():
    #     if agent.player_id == 1:
    #         print(f"agent enemy: {agent.id}", file=sys.stderr, flush=True)
#endregion

#region help

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    #print(f"own agent: {i}", file=sys.stderr, flush=True)

    # One line per agent: <agentId>;<action1;action2;...> actions are "MOVE x y | SHOOT id | THROW x y | HUNKER_DOWN | MESSAGE text"
#endregion