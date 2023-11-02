# Write your solution here

def longest_series_of_neighbours(my_list: list) -> int:
    max_longest = 1
    curr_longest = 1
    for i in range(len(my_list)-1):
        if abs(my_list[i]-my_list[i+1]) == 1:
            curr_longest += 1
        else:
            curr_longest = 1
        max_longest = max(max_longest, curr_longest)
    return max_longest

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
