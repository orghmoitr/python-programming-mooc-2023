# Write your solution here

def is_prime(num: int):
    if num == 2:
        return True
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True


def prime_numbers():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1


if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))
