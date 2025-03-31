from .core import CellState, Coord
BOARD_N = 8
"""
python -m search < test-vis1.csv
python -m search < test-vis2.csv
python -m search < test-vis3.csv
"""
# Find start cell (where red frog is)
def find_init_cell(board):
    for r in range(BOARD_N):
        for c in range(BOARD_N):
            cell_state = board.get(Coord(r, c), None)
            if cell_state == CellState.RED:
                start_cell = (r, c)
                print(start_cell)
                return start_cell
    print("No start point.")
    return None

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
def get_jump_cell(curr_cell, blue_cell):
    x = curr_cell.__getattribute__("r")
    y = curr_cell.__getattribute__("c")
    i = blue_cell.__getattribute__("r")
    j = blue_cell.__getattribute__("c")
    new_cell_x = i - (x - i)
    new_cell_y = j - (y - j)
    new_cell = Coord(new_cell_x, new_cell_y)
    print("New position is: ")
    print(new_cell)
    
    return new_cell

# Find all goals from board
def create_goal_list(board):
    goal_list = []
    for c in range(BOARD_N):
        cell_state = board.get(Coord(7, c), None)
        if cell_state == CellState.LILY_PAD:
            goal_list.append(Coord(7, c))
    print(goal_list)
    return goal_list

# Calculate the heuristic value of a cell
# Find min value of h from list of goals
def cal_manhattan_h(goal_list, curr_cell):
    x = curr_cell.__getattribute__("r")
    y = curr_cell.__getattribute__("c")
    i = goal_list[0].__getattribute__("r")
    j = goal_list[0].__getattribute__("c")
    min_f = abs(x - i) + abs(y - j)
    for goal in goal_list:
        i = goal.__getattribute__("r")
        j = goal.__getattribute__("c")
        f = abs(x - i) + abs(y - j)
        if(f < min_f):
            min_f = f
    print(min_f)
    return min_f

# Find list of cells that red frog can move next
def get_reachable_cells(board, curr_cell):
    # delete_in_list(curr_cell)
    reachable_cells = []
    x = curr_cell.__getattribute__("r")
    y = curr_cell.__getattribute__("c")
    i = x - 1
    j = y - 1
    while i < x + 2:
        while j < y + 2:
            if not(i == x and j == y):
                next_cell = Coord(i, j)
                # Check whether new_cell is where the blue frog is
                if is_jump(board, next_cell):
                    next_cell = get_jump_cell(curr_cell, next_cell)
                # Check whether is valid to move next(is lily_pad?)
                if is_lily_pad(board, next_cell):           
                    reachable_cells.append(next_cell)
            j = j + 1
        j = y - 1
        i = i + 1
    print(reachable_cells)
    return reachable_cells
