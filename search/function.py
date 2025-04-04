from .core import CellState, Coord, Direction, MoveAction
import math
BOARD_N = 8

# Define the Cell class
class Cell:
    def __init__(self):
        self.parent_i = 0
        self.parent_j = 0
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0  
    
# Find start cell (where red frog is)
def find_init_cell(board, cell_details):
    for r in range(BOARD_N):
        for c in range(BOARD_N):
            cell_state = board.get(Coord(r, c), None)
            if cell_state == CellState.RED:
                start_cell = Coord(r, c)
                cell_details[r][c].f = 0
                cell_details[r][c].g = 0
                cell_details[r][c].parent_i = r
                cell_details[r][c].parent_j = c 
                return start_cell
    return None

# Find cell that has lowest f in open_list
def find_lowest_f_cell(open_list, cell_details):
    x = open_list[0].__getattribute__("r")
    y = open_list[0].__getattribute__("c")
    lowest_cell = open_list[0]
    min_f = cell_details[x][y].f
    for cell in open_list:
        x = cell.__getattribute__("r")
        y = cell.__getattribute__("c")
        if cell_details[x][y].f < min_f:
            lowest_cell = cell
            min_f = cell_details[x][y].f
    return lowest_cell

# Find if cell is in position where blue frog is
def is_jump(board, cell):
    cell_state = board.get(cell)
    if cell_state == CellState.BLUE:
        return True
    else: 
        return False
    
# Find if cell is in position where lily pad is
def is_lily_pad(board, cell):
    cell_state = board.get(cell)
    if cell_state == CellState.LILY_PAD:
        return True
    else: 
        return False

# Get position of the cell after red frog jump over blue frog
# x and y are coordinate of current cell 
def get_jump_cell(x, y, blue_cell):
    i = blue_cell.__getattribute__("r")
    j = blue_cell.__getattribute__("c")
    new_cell_x = i - (x - i)
    new_cell_y = j - (y - j)
    if is_cell_in_board(new_cell_x , new_cell_y):
        new_cell = Coord(new_cell_x, new_cell_y)
    else:
        return None
    return new_cell

# Find all goals from board
def create_goal_list(board):
    goal_list = []
    for c in range(BOARD_N):
        cell_state = board.get(Coord(7, c), None)
        if cell_state == CellState.LILY_PAD:
            goal_list.append(Coord(7, c))
    return goal_list

# Calculate the g value of a cell
# i and j are the coordinates of a parent cell
def cal_g_value(cell_details, i, j):
    g = cell_details[i][j].g + 1.0
    return g

# Calculate the f value of a cell
def cal_f_value(g, h):
    return g + h

# Calculate the heuristic value of a cell
# Find min value of h from list of goals
# x, y are the coordinate of cell
def cal_euclidean_h(goal_list, x, y):
    i = goal_list[0].__getattribute__("r")
    j = goal_list[0].__getattribute__("c")
    min_h = abs(x - i) + abs(y - j)
    for goal in goal_list:
        i = goal.__getattribute__("r")
        j = goal.__getattribute__("c")
        h = math.sqrt((x - i)*(x - i) + (y - j)*(y - j))
        if(h < min_h):
            min_h = h
    return float(min_h)

# Determine if coordinate of cell is in range of BOARD_N
def is_cell_in_board(i ,j):
    if i > 7 or i < 0 or j > 7 or j < 0:
        return False
    else:
        return True

# Find list of cells that red frog can move next
# x, y are the coordinate of cell
def get_reachable_cells(board, x, y):
    reachable_cells = []
    i = x
    j = y - 1
    while i < x + 2:
        while j < y + 2:
            if not(i == x and j == y) and is_cell_in_board(i ,j):
                next_cell = Coord(i, j)
                
                # Check whether new_cell is where the blue frog is
                if is_jump(board, next_cell):
                    next_cell = get_jump_cell(x, y, next_cell)
                
                # Check whether is valid to move next(is lily_pad?)
                if is_lily_pad(board, next_cell) and next_cell != None:           
                    reachable_cells.append(next_cell)
            j = j + 1
        j = y - 1
        i = i + 1
    
    return reachable_cells

def get_direction(curr_x, curr_y, next_x, next_y):
    direction_x = next_x - curr_x 
    direction_y = next_y - curr_y
    
    if direction_x != 0: 
        direction_x = direction_x / abs(direction_x)
    if direction_y != 0: 
        direction_y = direction_y / abs(direction_y)
    
    return Direction(direction_x, direction_y) 

def find_path(cell_details, x, y, goal):
    path_list = []

    # Add the last cell to list
    goal_x = goal.__getattribute__("r")
    goal_y = goal.__getattribute__("c") 

    path_list.append(MoveAction(Coord(x, y), get_direction(x, y, goal_x, goal_y)))

    while not (cell_details[x][y].parent_i == x and cell_details[x][y].parent_j == y):
        temp_x = cell_details[x][y].parent_i
        temp_y = cell_details[x][y].parent_j
        path_list.append(MoveAction(Coord(temp_x, temp_y), get_direction(temp_x, temp_y, x, y)))
        x = temp_x
        y = temp_y

    path_list.reverse()

    return path_list