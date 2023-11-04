# write your solution here

def get_matrix() -> list:
    matrix = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            row = line.split(",")
            matrix.append(row)
    return matrix


def matrix_sum() -> int:
    total = 0
    for row in row_sums():
        total += row
    return total


def matrix_max() -> int:
    desired_value = 0
    for row in get_matrix():
        for number in row:
            if int(number) > desired_value:
                desired_value = int(number)
    return desired_value


def row_sums() -> list:
    desired_row = []
    for row in get_matrix():
        row_sum = 0
        for number in row:
            row_sum += int(number)
        desired_row.append(row_sum)
    return desired_row

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
