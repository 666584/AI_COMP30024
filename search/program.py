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

    """
    Yurim Cho's Note
    # Remember to delete all nodes that was used  
    # Find next_move from positions_to_move_list that has the lowest value of h
    # To Do: Think about how to deal with the next_moves that have same lowest value
    def find_next_move(goal_list, positions_to_move_list):
        min_h = cal_manhattan_h(goal_list, positions_to_move_list[0])
        next_move = positions_to_move_list[0]
        for next_position in positions_to_move_list:
            h = cal_manhattan_h(goal_list, next_position)
            # h <= min_h is acceptable
            if (h < min_h):
                next_move = next_position
                min_h = h
        return next_move
    """
    
    find_init_cell(board)
    print("Is next cell jump?")
    print(is_jump(board, Coord(3, 4)))
    get_jump_cell(Coord(2,2), Coord(3, 3))
    goal_list = create_goal_list(board)
    cal_manhattan_h(goal_list, Coord(3, 3))
    get_reachable_cells(board, Coord(2, 3))

    # Here we're returning "hardcoded" actions as an example of the expected
    # output format. Of course, you should instead return the result of your
    # search algorithm. Remember: if no solution is possible for a given input,
    # return `None` instead of a list.
    return [
        MoveAction(Coord(0, 5), [Direction.Down]),
        MoveAction(Coord(1, 5), [Direction.DownLeft]),
        MoveAction(Coord(3, 3), [Direction.Left]),
        MoveAction(Coord(3, 2), [Direction.Down, Direction.Right]),
        MoveAction(Coord(5, 4), [Direction.Down]),
        MoveAction(Coord(6, 4), [Direction.Down]),
    ]
