# COMP30024 Artificial Intelligence, Semester 1 2025
# Project Part A: Single Player Freckers

from .core import CellState, Coord, Direction, MoveAction
from .utils import render_board
from .function import *

def search(
    board: dict[Coord, CellState]
) -> list[MoveAction] | None:
    """
    This is the entry point for your submission. You should modify this
    function to solve the search problem discussed in the Part A specification.
    See `core.py` for information on the types being used here.

    Parameters:
        `board`: a dictionary representing the initial board state, mapping
            coordinates to "player colours". The keys are `Coord` instances,
            and the values are `CellState` instances which can be one of
            `CellState.RED`, `CellState.BLUE`, or `CellState.LILY_PAD`.
    
    Returns:
        A list of "move actions" as MoveAction instances, or `None` if no
        solution is possible.
    """

    # The render_board() function is handy for debugging. It will print out a
    # board state in a human-readable format. If your terminal supports ANSI
    # codes, set the `ansi` flag to True to print a colour-coded version!
    print(render_board(board, ansi=True))

    # Do some impressive AI stuff here to find the solution...
    # ...
    # ... (your solution goes here!)
    # ... 


    cell_details = [[Cell() for _ in range(BOARD_N)] for _ in range(BOARD_N)]

    # Init open_list and closed_list
    init_cell = find_init_cell(board, cell_details)
    if not init_cell: 
        return None
    open_list = [find_init_cell(board, cell_details)]
    closed_list = [[False for _ in range(BOARD_N)] for _ in range(BOARD_N)]

    # Init goal_list
    goal_list = create_goal_list(board)

    found_dest = False

    while len(open_list) > 0:
        curr_cell = find_lowest_f_cell(open_list, cell_details)
        
        open_list.remove(curr_cell)

        i = curr_cell.__getattribute__("r")
        j = curr_cell.__getattribute__("c")
        closed_list[i][j] = True
        reachable_cells = get_reachable_cells(board, i, j)

        for reachable_cell in reachable_cells:
            x = reachable_cell.__getattribute__("r")
            y = reachable_cell.__getattribute__("c")
            if not closed_list[x][y]:
                for goal in goal_list:
                    if reachable_cell == goal:

                        path = find_path(cell_details, i, j, goal)

                        found_dest = True
                        return path
                new_h = cal_euclidean_h(goal_list, x, y)
                new_g = cal_g_value(cell_details, i, j)
                new_f = cal_f_value(new_g, new_h)

                # If the cell is not in the open list or the new f value is smaller
                if cell_details[x][y].f == float('inf') or new_f < cell_details[x][y].f:
                    open_list.append(reachable_cell)
                    cell_details[x][y].h = new_h
                    cell_details[x][y].g = new_g
                    cell_details[x][y].f = new_f
                    cell_details[x][y].parent_i = i
                    cell_details[x][y].parent_j = j

    if not found_dest:
        return None