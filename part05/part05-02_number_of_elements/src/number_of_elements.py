# Write your solution here

def count_matching_elements(my_matrix: list, element: int) -> int:
    matching_elements = 0
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[i])):
            if my_matrix[i][j] == element:
                matching_elements += 1
            j += 1
        i += 1
    return matching_elements

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
