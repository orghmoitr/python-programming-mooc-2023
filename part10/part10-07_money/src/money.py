# TEE RATKAISUSI TÄHÄN:

class Money:

    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"

    def __eq__(self, another: "Money"):
        return self.__euros == another.__euros and self.__cents == another.__cents

    def __lt__(self, another: "Money"):
        if self.__euros == another.__euros:
            return self.__cents < another.__cents
        return self.__euros < another.__euros

    def __gt__(self, another: "Money"):
        if self.__euros == another.__euros:
            return self.__cents > another.__cents
        return self.__euros > another.__euros

    def __add__(self, another: "Money"):
        euros = self.__euros + another.__euros
        cents = self.__cents + another.__cents
        if cents >= 100:
            euros += 1
            cents -= 100
        return Money(euros, cents)

    def __sub__(self, another: "Money"):
        euros = self.__euros - another.__euros
        if euros < 0:
            raise ValueError("value of Money object cannot be negative")
        cents = self.__cents - another.__cents
        if cents < 0:
            euros -= 1
            if euros < 0:
                raise ValueError("value of Money object cannot be negative")
            cents = 100 - abs(cents)
        return Money(euros, cents)

    
if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2
    
    print(e3)
    print(e4)
    
    e5 = e2-e1
