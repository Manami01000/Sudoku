import tkinter as tk
from sudoku_solver import Sudoku

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sudoku")

        # Heading
        heading_label = tk.Label(master, text="Sudoku", font=("Arial", 20, "bold"))
        heading_label.pack(pady=10)

        # Separator
        separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
        separator.pack(fill=tk.X, padx=5)

        # Difficulty selection
        difficulty_frame = tk.Frame(master)
        difficulty_frame.pack(pady=10)

        difficulty_label = tk.Label(difficulty_frame, text="Difficulty: ")
        difficulty_label.pack(side=tk.LEFT)

        def select_difficulty(difficulty):
            sdk.sudoku_generator(difficulty)
            self.draw_grid()

        easy_button = tk.Button(difficulty_frame, text="Easy", command=lambda: select_difficulty(0))
        easy_button.pack(side=tk.LEFT, padx=10)

        medium_button = tk.Button(difficulty_frame, text="Medium", command=lambda: select_difficulty(1))
        medium_button.pack(side=tk.LEFT, padx=10)

        hard_button = tk.Button(difficulty_frame, text="Hard", command=lambda: select_difficulty(2))
        hard_button.pack(side=tk.LEFT, padx=10)

        # Sudoku grid
        self.grid_frame = tk.Frame(master)
        self.grid_frame.pack()

        self.grid_widgets = [[None for _ in range(9)] for _ in range(9)]

        # Solve button
        solve_button = tk.Button(master, text="Solve", command=self.solve)
        solve_button.pack(pady=10)

        # Initialize Sudoku instance
        sdk = Sudoku(generate=1)
        sdk.sudoku_generator(difficulty=1)
        self.sdk = sdk

        self.draw_grid()

    def draw_grid(self):
        sdk = self.sdk

        for i in range(9):
            for j in range(9):
                value = sdk.matrix[i][j]

                if value == 0:
                    value = ""

                if self.grid_widgets[i][j] is None:
                    self.grid_widgets[i][j] = tk.Entry(self.grid_frame, width=2, font=("Arial", 20), justify="center")
                    self.grid_widgets[i][j].grid(row=i, column=j, padx=1, pady=1)

                self.grid_widgets[i][j].delete(0, tk.END)
                self.grid_widgets[i][j].insert(0, str(value))

    def solve(self):
        sdk = self.sdk
        sdk.solver()
        self.draw_grid()

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
