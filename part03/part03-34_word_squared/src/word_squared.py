# Write your solution here

def squared(text, times):
    row = text * (times * times)
    i = 0
    j = times
    count = 0
    while count < times:
        print(row[i:j])
        i += times
        j += times
        count += 1

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
