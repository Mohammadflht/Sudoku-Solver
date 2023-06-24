import time

class SudokuSolver:
    def __init__(self, puzzle):  # takes a puzzle as input and initializes the object's puzzle attribute with it
        self.puzzle = puzzle     # recursively solves the Sudoku puzzle using backtracking

    def solve(self):
        return self._solve()

    def _solve(self):
        empty_cell, candidates = self._find_empty_cell()    # Find empty cells and possible candidates for it
        if not empty_cell:
            return True                       # If there is no empty cell, it means Sudoku is solved

        row, col = empty_cell                 # else gets the empty cell row and column

        for num in candidates:                # Checks all candidates
            self.puzzle[row][col] = num       # Places Candidate in empty cell

            if self._solve():                 # Recursive
                return True                   # If solved correctly return true

            self.puzzle[row][col] = 0         # else empties the cell again

        return False

    def _find_empty_cell(self):     # find an empty cell and applies MRV and Degree Heuristic to determine the best candidate for that cell
        # Apply MRV and Degree Heuristic
        min_values = float('inf')                             # Set the initial value to infinity
        min_cell = None                                       # set the initial value of the empty cell to none
        candidate = []                                        # List of candidates
        for row in range(9):
            for col in range(9):
                if self.puzzle[row][col] == 0:                # If the cell was empty
                    temp = self._get_candidates(row, col)
                    num_values = len(temp)                    # put the length of the candidates into the num_values
                    if num_values < min_values:
                        min_values = num_values
                        min_cell = (row, col)
                        candidate = temp

        return min_cell, candidate    # returns a tuple containing the coordinates of the best empty cell (i.e., with the fewest possible candidates) and its corresponding candidate list

    def _get_candidates(self, row, col):
        candidates = set(range(1, 10))

        for i in range(9):
            candidates.discard(self.puzzle[row][i])  # Remove numbers in the same row
            candidates.discard(self.puzzle[i][col])  # Remove numbers in the same column

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                candidates.discard(self.puzzle[start_row + i][start_col + j])  # Remove numbers in the same box

        return candidates

    def print_solution(self):
        output = ''
        for row in self.puzzle:
            output += (" ".join(str(num) for num in row)) + '\n'
        return output


def read_input_file(filename):
    puzzle = []
    with open(filename, "r") as file:
        for line in file:
            row = [int(num) for num in line.split()]
            puzzle.append(row)
    return puzzle


if __name__ == "__main__":           # Checks if the current module is being run as the main program.
    puzzle = read_input_file("5.txt")
    solver = SudokuSolver(puzzle)

    start_time = time.perf_counter()
    solved = solver.solve()
    end_time = time.perf_counter()

    run_time = (end_time - start_time) * 1e9
    type_time = 'ns'
    if run_time / 1000000 > 1:
        run_time = run_time / 1000000
        type_time = 'ms'
        if run_time / 1000 > 1:
            run_time = run_time / 1000
            type_time = 's'

    with open('output.txt', 'w') as file:
        print(f'Time taken: {run_time:.2f} {type_time} to run.')
        file.write(f'Time taken: {run_time:.2f} {type_time} to run.\n')
        if solved:
            output = solver.print_solution()
            print(output)
            file.write(output)
        else:
            print("No solution exists for the given puzzle.")
            file.write("No solution exists for the given puzzle.\n")
