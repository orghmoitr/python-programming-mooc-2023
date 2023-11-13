# WRITE YOUR SOLUTION HERE:

class SimpleDate:

    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    def __eq__(self, another: "SimpleDate"):
        return (self.__day == another.__day and
                self.__month == another.__month and
                self.__year == another.__year)

    def __ne__(self, another: "SimpleDate"):
        return (self.__day != another.__day or
                self.__month != another.__month or
                self.__year != another.__year)

    def __lt__(self, another: "SimpleDate"):
        if self.__year == another.__year:
            if self.__month == another.__month:
                if self.__day == another.__day:
                    pass
                else:
                    return self.__day < another.__day
            else:
                return self.__month < another.__month
        else:
            return self.__year < another.__year

    def __gt__(self, another: "SimpleDate"):
        if self.__year == another.__year:
            if self.__month == another.__month:
                if self.__day == another.__day:
                    pass
                else:
                    return self.__day > another.__day
            else:
                return self.__month > another.__month
        else:
            return self.__year > another.__year

    def __add__(self, day: int):
        new_day = self.__day
        new_month = self.__month
        new_year = self.__year
        for i in range(day):
            new_day += 1
            if new_day > 30:
                new_month += 1
                new_day = 1
                if new_month > 12:
                    new_year += 1
                    new_month = 1
            print(f"{new_day}.{new_month}.{new_year}")
        return SimpleDate(new_day, new_month, new_year)

    def __sub__(self, another: "SimpleDate"):
        year_difference = abs(self.__year - another.__year)
        if year_difference == 0:
            return abs((self.__day + self.__month * 30) -
                       (another.__day + another.__month * 30))
        else:
            return abs((self.__day + self.__month * 30) -
                       (another.__day + another.__month * 30) +
                       ((self.__year - another.__year) * 360))


if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
