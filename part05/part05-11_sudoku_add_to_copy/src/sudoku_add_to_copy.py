# Write your solution here

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = []
    for i in range(len(sudoku)):
        row = []
        for j in range(len(sudoku[i])):
            row.append(sudoku[i][j])
        new_sudoku.append(row)
    new_sudoku[row_no][column_no] = number
    return new_sudoku

def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        if i > 0 and i % 3 == 0:
            print()
        for j in range(len(sudoku[i])):
            if j > 0 and j % 3 == 0:
                print(" ", end="")
            square = sudoku[i][j]
            if square > 0:
                print(f"{square} ", end="")
            else:
                print(f"_ ", end="")
        print()            

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
