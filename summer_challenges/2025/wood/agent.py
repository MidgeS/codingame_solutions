import sys
import math
from enum import Enum

#region definitions
class Agent:
    id = 0
    player_id = 0
    shoot_cooldown = 0
    optimal_range = 0
    soaking_power = 0
    splash_bombs = 0
    wetness = 0
    x = -1
    y = -1
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

class TileType(Enum):
    EMPTY = 0
    LOW_COVER = 1
    HIGH_COVER = 2

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        if self.__class__ is int:
            return self < other.value
        if other.__class__ is int:
            return self.value < other
        return NotImplemented
    
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        if self.__class__ is int:
            return self > other.value
        if other.__class__ is int:
            return self.value > other
        return NotImplemented
    
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        if self.__class__ is int:
            return self == other.value
        if other.__class__ is int:
            return self.value == other
        return NotImplemented

class Map:
    width = 0
    height = 0
    cells = []

    def __init__(self, width, height):
        self.width = width
        self.height = height
        for i in range(width*height):
            self.cells.append(TileType.EMPTY)

    def getIndex(self,x,y):
        return y*width + x

    def setCell(self,x,y,type):
        index = self.getIndex(x,y)
        self.cells[index] = type

    def getCell(self,x,y):
        if(x < 0 or x > self.width or y < 0 or y > self.height):
            return -1
        
        index = self.getIndex(x,y)
        return self.cells[index]
    
    def printMap(self):
        for y in range(height):
            line = ""
            for x in range(width):
                line += str(self.getCell(x,y))
            
            debugPrint(line)

def debugPrint(line):
    print(line, file=sys.stderr, flush=True)

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
    global my_id
    for i in range(agent_count):
        # cooldown: Number of turns before this agent can shoot
        # wetness: Damage (0-100) this agent has taken
        agent_id, x, y, cooldown, splash_bombs, wetness = [int(j) for j in input().split()]
        
        agents[agent_id].updatePosition(x,y)
        agents[agent_id].updateCooldown(cooldown)
        agents[agent_id].updateSplashBombs(splash_bombs)
        agents[agent_id].updateWetness(wetness)
        if(agents[agent_id].player_id == my_id):
            own_active_agents[agent_id] = agents[agent_id]
        else:
            enemy_active_agents[agent_id] = agents[agent_id]

def findTargetAgent(agent: Agent, enemy_agents: dict[int,Agent]):
    #find agents in optimal range
    in_range : list[Agent] = []
    for enemy in enemy_agents.values():
        dist = calculateDistance((agent.x, agent.y), (enemy.x, enemy.y))
        if dist <= agent.optimal_range:
            in_range.append(enemy)
    #then pick one with least cover
    global map
    best_target = -1
    target_cover = 3
    # for enemy_in_range in in_range:
    #     cover = findLeastCover(enemy, map)
    #     if cover[0] >= 0 and cover[1] >= 0 and map.getCell(cover[0], cover[1]) < target_cover:
    #         best_target = enemy_in_range

    # loop over targetable
    # only check cover in direction of target
    # pick targett with least cover in target direction
    for enemy_in_range in in_range:
        debugPrint(f"checking enemy {enemy_in_range.x},{enemy_in_range.y}")
        cover = findCoverBetweenAgentAndTarget(agent, enemy_in_range, map)
        debugPrint(f"best cover found at {cover[0]},{cover[1]} - cover: {cover[2]}")
        if cover[0] >= 0 and cover[1] >= 0 and (cover_cell := map.getCell(cover[0], cover[1])) < target_cover:
            debugPrint(f"new best cover - cell: {cover_cell}")
            target_cover = cover_cell
            best_target = enemy_in_range
        if cover[0] == -1 and cover[1] == -1:
            target_cover = 0
            best_target = enemy_in_range

    return best_target

def isAgentAdjacentToCover(agent: Agent, cell: tuple[int,int]):
    adjacent = False

    if agent.x == cell[0] - 1 and agent.y == cell[1] : adjacent = True
    if agent.x == cell[0] + 1 and agent.y == cell[1] : adjacent = True
    if agent.x == cell[0] and agent.y == cell[1] - 1 : adjacent = True
    if agent.x == cell[0] and agent.y == cell[1] - 2 : adjacent = True

    return adjacent


def findCoverBetweenAgentAndTarget(agent: Agent, enemy: Agent, map: Map):
    #get direction vector
    x_dir = max(-1, min(1, agent.x - enemy.x))
    y_dir = max(-1, min(1, agent.y - enemy.y))
    
    debugPrint(f"dir vector {x_dir},{y_dir}")

    x_coord = (enemy.x + x_dir, enemy.y)
    y_coord = (enemy.x, enemy.y + y_dir)

    #check all cells adjacent to enemy in vector directions
    x_cell = map.getCell(enemy.x + x_dir, enemy.y)
    y_cell = map.getCell(enemy.x, enemy.y + y_dir)

    debugPrint(f"x cell {enemy.x + x_dir},{enemy.y} - {x_cell}")
    debugPrint(f"y cell {enemy.x},{enemy.y + y_dir} - {y_cell}")

    #if cell is cover check if agent is next to that cover respecting direction vector
    x_cover = y_cover = 0
    if x_cell == TileType.LOW_COVER or x_cell == TileType.HIGH_COVER:
        #check if agent next to cover
        if not isAgentAdjacentToCover(agent, x_coord):
            x_cover = x_cell
    if y_cell == TileType.LOW_COVER or y_cell == TileType.HIGH_COVER:
        #check if agent next to cover
        if not isAgentAdjacentToCover(agent, y_coord):
            y_cover = y_cell

    if x_cover > 0 and x_cover >= y_cover:
        return (enemy.x + x_dir, enemy.y, x_cover)
    if y_cover > 0 and y_cover > x_cover:
        return (enemy.x, enemy.y + y_dir, x_cover)
    
    return (-1,-1, 0)

def getBestCellCover(cell_coords, map: Map):

    
    debugPrint(f"search cell {cell_coords}")
    cover_value = TileType.EMPTY
    top_cell = map.getCell(cell_coords[0], cell_coords[1] - 1)
    if top_cell != -1 and top_cell > cover_value:
        debugPrint(f"top is cover")
        cover_value = top_cell
    bottom_cell = map.getCell(cell_coords[0], cell_coords[1] + 1)
    if bottom_cell != -1 and bottom_cell > cover_value:
        debugPrint(f"bottom is cover")
        cover_value = bottom_cell
    left_cell = map.getCell(cell_coords[0] - 1, cell_coords[1])
    if left_cell != -1 and left_cell > cover_value:
        debugPrint(f"left is cover")
        cover_value = left_cell
    right_cell = map.getCell(cell_coords[0] + 1, cell_coords[1])
    if right_cell != -1 and right_cell > cover_value:
        debugPrint(f"right is cover")
        cover_value = right_cell

    return cover_value

def findNeighboringCovers(agent: Agent, map: Map, cellCoverFunction):
    covers = []

    #this level only requires checking neighboring cells in cross pattern
    #find cover in neighbor cells
    top_cell = cellCoverFunction((agent.x, agent.y - 1), map)
    if top_cell == TileType.HIGH_COVER or top_cell == TileType.LOW_COVER:
        debugPrint("top cell has cover")
        covers.append((agent.x, agent.y-1, top_cell))
    bottom_cell = cellCoverFunction((agent.x, agent.y+1), map)
    if bottom_cell == TileType.HIGH_COVER or bottom_cell == TileType.LOW_COVER:
        debugPrint("bottom cell has cover")
        covers.append((agent.x, agent.y+1, bottom_cell))
    left_cell = cellCoverFunction((agent.x-1, agent.y), map)
    if left_cell == TileType.HIGH_COVER or left_cell == TileType.LOW_COVER:
        debugPrint("left cell has cover")
        covers.append((agent.x-1, agent.y, left_cell))
    right_cell = cellCoverFunction((agent.x+1, agent.y), map)
    if right_cell == TileType.HIGH_COVER or right_cell == TileType.LOW_COVER:
        debugPrint("right cell has cover")
        covers.append((agent.x+1, agent.y, right_cell))

    return covers        

def findBestCover(agent: Agent, map: Map):
    #find closest cover and pick highest cover if multiple
    covers = findNeighboringCovers(agent, map, getBestCellCover)

    cover_value = 0
    cover_coords = (-1,-1)

    for cover in covers:
        debugPrint(f"agent cover: {cover}")
        if cover[2] > cover_value:
            cover_value = cover[2]
            cover_coords = cover[:2]

    return cover_coords

def findLeastCover(agent: Agent, map: Map):
    #find closest cover and pick highest cover if multiple
    covers = findNeighboringCovers(agent, map, getBestCellCover) #TODO least cell cover

    cover_value = 3
    cover_coords = (-1,-1)

    for cover in covers:
        cell_type = map.getCell(cover[0], cover[1])
        if cell_type < cover_value:
            cover_value = cell_type
            cover_coords = cover

    return cover_coords

#region current dev
def findEnclosedAgentAndArea(agents : dict[int, Agent], areas, my_id):
    for agent in agents.values():
        if agent.player_id == my_id:
            for area in range(len(areas)):
                if agentAdjacentToCell(agent, (areas[area][0], areas[area][1])):
                    return (agent, area)

    return (-1, -1)

def agentAdjacentToCell(agent: Agent, cell: tuple[int,int]):
    
    return cell[0] - 1 <= agent.x <= cell[0] + 1 and cell[1] - 1 <= agent.y <= cell[1] + 1

def agentInArea(agent: Agent, center: tuple[int, int], distance):
    return center[0] - distance <= agent.x <= center[0] + distance and center[1] - distance <= agent.y <= center[1] + distance

def findBombTargetInArea(agents: dict[int,Agent], area: tuple[int,int,bool]):
    #find target in area with most enemy hits
    #target is not valid if own agent would be hit
    max_target_count = 0
    target = None
    for x in range(area[0]-1, area[0]+2):
        for y in range(area[1]-1, area[1]+2):
            debugPrint(f"target in area: {x} {y}")
            target_count = 0
            for agent in agents.values():
                if agentInArea(agent, (x,y), 1):
                    global my_id
                    if agent.player_id == my_id:
                        debugPrint("whould hit itself")
                        break
                    target_count += 1
            else:
                debugPrint(f"targets: {target_count}")
                if target_count > max_target_count:
                    target = (x,y)
                continue
    return target
#endregion

#region game logic
agents = {}

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

areas = [(2, 2, False), (map.width-3, 2, False), (2, map.height-3, False), (map.width-3, map.height-3, False)]

agent_target = None
target_area = None

#region game loop
while True:
    agent_count = int(input())  # Total number of agents still in the game

    enemy_active_agents = {}
    own_active_agents = {}
    
    readActiveAgentData(agent_count)

    my_agent_count = int(input())  # Number of alive agents controlled by you
    
    agent_and_area = findEnclosedAgentAndArea(agents, areas, my_id)
    debugPrint(f"agent {agent_and_area[0].id} in area {agent_and_area[1]} at {areas[agent_and_area[1]]}")

    agent: Agent
    for agent in own_active_agents.values():
        agent_command = f"{agent.id};"
        if agent.player_id == my_id:
            if agent.id == agent_and_area[0].id:
                agent_command += f"MOVE {agent.x} {agent.y};"
                debugPrint(f"splash bombs in area: {agent.splash_bombs}")
                #if agent.splash_bombs > 0:
                 #   bomb_target = findBombTargetInArea(agents, areas[agent_and_area[1]])
                  #  if bomb_target:
                   #     agent_command += f"THROW {bomb_target[0]} {bomb_target[1]}"
                    #pass
            else:
                
                debugPrint(f"splash bombs moving: {agent.splash_bombs}")
                #move to populated area and throw bomb if close
                if agent_target:
                    # if close enough throw bomb and clear target else keep moving
                    dist = calculateDistance((agent.x, agent.y),agent_target)
                    if dist <= 4:
                        agent_command += f"MOVE {agent.x} {agent.y};"
                        agent_command += f"THROW {agent_target[0]} {agent_target[1]};"
                        areas[target_area] = (areas[target_area][0], areas[target_area][1], True)
                        agent_target = None
                    else:
                        agent_command += f"MOVE {agent_target[0]} {agent_target[1]};"
                else:
                    #pick new target
                    # improve to pick closest first to prevent needles running around and wasting rounds
                    for x in range(len(areas)):
                        if x != agent_and_area[1] and areas[x][2] == False:
                            target_area = x
                            agent_target = (areas[x][0], areas[x][1])
                            agent_command += f"MOVE {agent_target[0]} {agent_target[1]};"
                            break

            print(agent_command)
            
#endregion
#endregion

#region help

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    #print(f"own agent: {i}", file=sys.stderr, flush=True)

    # One line per agent: <agentId>;<action1;action2;...> actions are "MOVE x y | SHOOT id | THROW x y | HUNKER_DOWN | MESSAGE text"
#endregion

#region notes
    # hardcode areas and centers?
    # find area with agent inside and throw there
    # other agent runs all other 3 areas and throws bombs
#endregion