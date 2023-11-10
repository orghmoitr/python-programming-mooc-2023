# Write your solution here:

class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0
        
    def tick(self):
        self.seconds += 1
        if self.seconds > 59:
            self.minutes += 1
            self.seconds = 0
            if self.minutes > 59:
                self.minutes = 0
                self.hours = 0
                self.seconds = 0
        
    def __str__(self):
        return f"{self.hours:02.0f}:{self.minutes:02.0f}:{self.seconds:02.0f}"

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)
