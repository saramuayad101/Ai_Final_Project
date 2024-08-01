import tkinter as tk
import numpy as np

#our sudoku board 
board=np.array([
    [0, 0, 6, 0, 1, 9, 0, 0, 0],
    [0, 7, 2, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 8, 0, 5, 1],
    [0, 1, 0, 0, 0, 4, 0, 2, 6],
    [0, 0, 0, 9, 5, 0, 0, 7, 0],
    [3, 0, 0, 0, 2, 0, 5, 0, 8],
    [8, 0, 9, 3, 0, 0, 0, 0, 0],
    [0, 5, 0, 7, 0, 0, 3, 9, 0],
    [4, 0, 0, 0, 0, 6, 2, 0, 0]
])


# Function to solve it
def solve(bo):
    find = find_empty(bo)  # Find an empty space
    if not find:  # If not puzzle is solved
        return True
    else:
        row, col = find  # Get the row and column of the empty space

    for i in range(1, 10):  # Try numbers 1 through 9
        if valid(bo, i, (row, col)):  # Check if the number is valid
            bo[row, col] = i  # Place the number

            if solve(bo):  # Recursively try to solve the board
                return True

            bo[row, col] = 0  # Reset the space if it didn't lead to a solution

    return False

# checking if a number is valid 
def valid(bo, num, pos):
    # Check the row
    for i in range(len(bo[0])):
        if bo[pos[0], i] == num and pos[1] != i:
            return False

    # Check the column
    for i in range(len(bo)):
        if bo[i, pos[1]] == num and pos[0] != i:
            return False

    # Check the 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i, j] == num and (i, j) != pos:
                return False

    return True

#finding an empty space on our board
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i, j] == 0:
                return (i, j)  # Return row and column of the empty space

    return None



# displaying the Sudoku board with Tkinter canvas
def display_board(canvas, bo, offset_x, offset_y):
    cell_size = 50
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            x0 = offset_x + j * cell_size
            y0 = offset_y + i * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size
            canvas.create_rectangle(x0, y0, x1, y1, width=1)
            if bo[i, j] != 0:
                canvas.create_text(x0 + cell_size / 2, y0 + cell_size / 2, text=str(bo[i, j]), font=('Arial', 18))

#drawing thicker lines for 3x3 sections to make it look nicer
def draw_grid_lines(canvas, offset_x, offset_y):
    cell_size = 50
    for i in range(0, 10):
        width = 3 if i % 3 == 0 else 1
        canvas.create_line(offset_x, offset_y + i * cell_size, offset_x + 9 * cell_size, offset_y + i * cell_size, width=width)
        canvas.create_line(offset_x + i * cell_size, offset_y, offset_x + i * cell_size, offset_y + 9 * cell_size, width=width)

#solve the board and update the display
def solve_and_display(canvas, offset_x, offset_y):
    solve(board)  # Solve the board
    display_board(canvas, board, offset_x, offset_y)  # Display the solved board

# Create the main window
root = tk.Tk()
root.title("Sudoku Solver")

#using canvas to display the Sudoku boards
canvas = tk.Canvas(root, width=1100, height=550)
canvas.pack()

# before solving
offset_before_x = 20
offset_before_y = 40
canvas.create_text(offset_before_x + 200, offset_before_y - 15, text="Before Solving", font=('Arial', 18))
display_board(canvas, board, offset_before_x, offset_before_y)
draw_grid_lines(canvas, offset_before_x, offset_before_y)

# afterSolving the board 
offset_after_x = 600
offset_after_y = 40
canvas.create_text(offset_after_x + 200, offset_after_y - 15, text="After Solving", font=('Arial', 18))
solve_and_display(canvas, offset_after_x, offset_after_y)
draw_grid_lines(canvas, offset_after_x, offset_after_y)


root.mainloop()