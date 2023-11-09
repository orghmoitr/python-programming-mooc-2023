# Write your solution here!

class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
        self.my_sum = 0

    def add_number(self, number:int):
        self.count += 1
        self.my_sum += number

    def count_numbers(self):
        return self.count

    def get_sum(self):
        if self.count == 0:
            return 0
        return self.my_sum

    def average(self):
        if self.count > 0:
            return self.my_sum / self.count

def main():
    stats = NumberStats()
    even_stats = NumberStats()
    odd_stats = NumberStats()
    
    print("Please type in integer numbers:")
    while True:
        number = int(input(""))
        if number == -1:
            break
        elif number % 2 == 0:
            even_stats.add_number(number)
        else:
            odd_stats.add_number(number)
        stats.add_number(number)
        

    print(f"Sum of numbers: {stats.get_sum()}")
    print(f"Mean of numbers: {stats.average()}")
    print(f"Sum of even numbers: {even_stats.get_sum()}")
    print(f"Sum of odd numbers: {odd_stats.get_sum()}")

main()
