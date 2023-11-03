# Write your solution here

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    row = sudoku[row_no]
    row[column_no] = number

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
    
    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)
