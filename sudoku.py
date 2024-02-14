from icecream import ic
from typing import List, Tuple, Optional

def find_next_empty(puzzle: List[List[int]]) -> Tuple[Optional[int], Optional[int]]:
    """
    Finds the next empty cell in the Sudoku puzzle.

    Args:
        puzzle (List[List[int]]): The Sudoku puzzle represented as a 9x9 grid.

    Returns:
        Tuple[Optional[int], Optional[int]]: The row and column indices of the next empty cell.
    """
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col
    return None, None 

def is_valid(puzzle: List[List[int]], guess: int, row: int, col: int) -> bool:
    """
    Checks if placing a guess in a cell is a valid move in the Sudoku puzzle.

    Args:
        puzzle (List[List[int]]): The Sudoku puzzle represented as a 9x9 grid.
        guess (int): The number to be placed in the cell.
        row (int): The row index of the cell.
        col (int): The column index of the cell.

    Returns:
        bool: True if the guess is valid, False otherwise.
    """
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True

def solve_sudoku(puzzle: List[List[int]]) -> bool:
    """
    Solves the Sudoku puzzle using backtracking.

    Args:
        puzzle (List[List[int]]): The Sudoku puzzle represented as a 9x9 grid.

    Returns:
        bool: True if the puzzle is solved, False otherwise.
    """
    row, col = find_next_empty(puzzle)

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True

        puzzle[row][col] = -1

    return False


if __name__ == "__main__":
    example_board: List[List[int]] = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

    ic(solve_sudoku(example_board))
    ic(example_board)
