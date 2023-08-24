
import numpy as np
import random

class Sudoku:
    def __init__(self, matrix=np.array([[0 for i in range(9)] for j in range(9)]), generate=-1):
        self.solved_sudoku = None
        if generate > -1:
            self.sudoku_generator(difficulty=generate)
        else:
            self.matrix = matrix
            self.solver()
            self.solved_sudoku = np.copy(self.matrix)
            self.matrix = matrix



# prints the matrix inside the file "txt"
    def sudoku_printer(self):
        text = open("txt", "a")
        # print("\n-------------------------")
        text.write("\n-------------------------\n")  # creates a border between 3 rows
        for j in range(9):
            for i in range(9):
                if (i + 1) % 3 == 0:  # creates a border between 3 columns
                    # print(self.matrix[j][i], end=" | ")
                    text.write(f"{self.solved_sudoku[j][i]} | ")

                elif i == 0:
                    # print("| %d" % self.matrix[j][i], end=" ")
                    text.write(f"| {self.solved_sudoku[j][i]} ")  # creates a line before the first column
                else:
                    # print(self.matrix[j][i], end=" ")
                    text.write(f"{self.solved_sudoku[j][i]} ")  # creates a space after each number
            if (j + 1) % 3 == 0:
                # print("\n-------------------------")
                text.write("\n-------------------------\n")   # creates a line before the first row
            else:
                # print("")
                text.write("\n")

    def sudoku_criteria(self, number, row, col):

        # row check: checks if there is any number in the row that's the same as "number"
        for i in self.matrix[row]:
            if i == number:
                return False
        # column check: checks if there is any number in the column that's the same as "number"
        for i in self.matrix[:, col]:
            if i == number:
                return False

        slice_col = (col // 3) * 3
        slice_row = (row // 3) * 3
        square = self.matrix[slice_row: slice_row + 3, slice_col: slice_col + 3]
        for i in square:
            for j in i:
                if j == number:
                    return False

        return True

    def sudoku_solver(self, row, col):
        if (row == 9):
            return True
        if (self.matrix[row][col] == 0):
            for k in random.sample(range(1, 10), 9):
                self.matrix[row][col] = 0
                meets_criteria = self.sudoku_criteria(k, row, col)
                if meets_criteria:
                    self.matrix[row][col] = k

                    if col == 8:
                        solved = self.sudoku_solver(row + 1, col=0)
                    else:
                        solved = self.sudoku_solver(row, col + 1)
                    if not solved:
                        continue
                    else:
                        return True
                else:
                    continue
            # self.sudoku_printer()
            self.matrix[row][col] = 0
            return False
        else:
            if col >= 8:
                solved = self.sudoku_solver(row + 1, col=0)
            else:
                solved = self.sudoku_solver(row, col + 1)
            return solved

    def sudoku_solver2(self, row, col):
        if (row == 9):
            return 1
        if (self.matrix[row][col] == 0):
            sum_solutions = 0
            for k in range(1, 10):
                self.matrix[row][col] = 0
                meets_criteria = self.sudoku_criteria(k, row, col)
                if meets_criteria:
                    self.matrix[row][col] = k

                    if col == 8:
                        solved = self.sudoku_solver2(row + 1, col=0)
                    else:
                        solved = self.sudoku_solver2(row, col + 1)
                    sum_solutions += solved
                else:
                    continue
            # self.sudoku_printer()
            self.matrix[row][col] = 0
            return sum_solutions
        else:
            if col == 8:
                solved = self.sudoku_solver2(row + 1, col=0)
            else:
                solved = self.sudoku_solver2(row, col + 1)
            return solved

    def solver(self):
        self.sudoku_solver(0, 0)
        # self.sudoku_printer()


    def solver2(self):
        if self.sudoku_solver2(0, 0) == 1:
            return True
        else:
            return False

    def sudoku_generator(self, difficulty):
        self.matrix = np.array([[0 for i in range(9)] for j in range(9)])
        self.solver()
        self.solved_sudoku = np.copy(self.matrix)
        difficulties = [range(30, 40), range(40, 49), range(49, 58)]
        blank_spaces = random.choice(difficulties[difficulty])
        rows = np.array(range(9))
        cols = np.array(range(9))
        x, y = np.meshgrid(rows, cols)
        matrix_combinations = np.column_stack((x.ravel(), y.ravel()))
        #random.sample(matrix_combinations, 81)
        np.random.shuffle(matrix_combinations)
        index = 0
        for i in range(blank_spaces):
            sol = False
            while not sol and index < 81:
                row, col = matrix_combinations[index]
                index += 1
                num_removed = self.matrix[row][col]
                self.matrix[row][col] = 0
                sol = self.solver2()
                if not sol:
                    self.matrix[row][col] = num_removed
        self.sudoku_printer()



if __name__ == "__main__":
    arr = np.array([ [8,2,7,1,5,4,3,9,6],
            [9,6,5,3,2,7,1,4,8],
            [3,4,1,6,8,9,7,5,2],
            [5,9,3,4,6,8,2,7,1],
            [4,7,2,5,1,3,6,8,9],
            [6,1,8,9,7,2,4,3,5],
            [7,8,6,2,3,5,9,1,4],
            [1,5,4,7,9,6,8,2,3],
            [2,3,9,8,4,1,5,6,7]])

    arr2 = np.array([[5,3,0,0,7,0,0,0,0],
                    [6,0,0,1,9,5,0,0,0],
                    [0,9,8,0,0,0,0,6,0],
                    [8,0,0,0,6,0,0,0,3],
                    [4,0,0,8,0,3,0,0,1],
                    [7,0,0,0,2,0,0,0,6],
                    [0,6,0,0,0,0,2,8,0],
                    [0,0,0,4,1,9,0,0,5],
                    [0,0,0,0,8,0,0,7,9]])
    sudoku2 = Sudoku(generate=2)
