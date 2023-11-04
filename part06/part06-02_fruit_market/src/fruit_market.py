# write your solution here

def read_fruits() -> dict:
    fruits = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruit = parts[0]
            price = float(parts[1])
            fruits[fruit] = price
    return fruits


if __name__ == "__main__":
    print(read_fruits())
