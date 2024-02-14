# Sudoku Solver

This is a simple Python program to solve Sudoku puzzles using backtracking algorithm.

## Introduction

Sudoku is a popular puzzle game played on a 9x9 grid. The goal is to fill the grid such that each row, each column, and each of the nine 3x3 subgrids contain all of the digits from 1 to 9 without repetition.

## Features

- Solves Sudoku puzzles using backtracking algorithm.
- Customizable input puzzles.
- Provides clear solution or indicates if the puzzle is unsolvable.

## How to Use

1. **Clone the repository:**

    ```bash
    git clone https://github.com/AnubhavShekhar/Sudoku-Solver.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd sudoku-solver
    ```

3. **Run the solver:**

    ```bash
    python sudoku_solver.py
    ```

4. **Follow the on-screen instructions to enter your Sudoku puzzle. Use `-1` to represent empty cells.**

## Usage Instructions

- The Sudoku puzzle is represented as a 9x9 grid. Use a 2D list to input your puzzle in the code.
- Each cell can contain a number from 1 to 9, or `-1` to represent an empty cell.
- Run the program and it will attempt to solve the puzzle. If a solution is found, it will print the solved puzzle. If not, it will indicate that the puzzle is unsolvable.
