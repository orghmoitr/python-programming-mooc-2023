# Write your solution here

def most_common_character(string: str) -> str:
    desired_char = string[0]
    most_occurrences = string.count(desired_char)
    for i in range(len(string)):
        if string.count(string[i]) > most_occurrences:
            desired_char = string[i]
            most_occurrences = string.count(string[i])
    return desired_char

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
    
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
