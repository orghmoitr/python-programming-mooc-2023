# write your solution here

def largest() -> int:
    # empty list to store numbers from file
    numbers = []

    # make a list of numbers from file contents
    with open("numbers.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            numbers.append(int(line))

    # find the largest number from the list
    largest_number = numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number    
            

if __name__ == "__main__":
    print(largest())

