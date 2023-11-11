# Write your solution here

class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max_weight: int):
        self.items = []
        self.max_weight = max_weight

    def add_item(self, item: Item):
        total_weight = self.weight() + item.weight()
        if total_weight <= self.max_weight:
            self.items.append(item)

    def weight(self):
        total = 0
        for item in self.items:
            total += item.weight()
        return total

    def __str__(self):
        print_result = ""
        if len(self.items) == 1:
            print_result += f"{len(self.items)} item ({self.weight()} kg)"
        else:
            print_result += f"{len(self.items)} items ({self.weight()} kg)"
        return print_result

    def print_items(self):
        for item in self.items:
            print(item)

    def heaviest_item(self):
        if len(self.items) == 0:
            return None
        heaviest = self.items[0]
        for item in self.items:
            if item.weight() > heaviest.weight():
                heaviest = item
        return heaviest


class CargoHold:
    def __init__(self, max_weight: int):
        self.suitcases = []
        self.max_weight = max_weight

    def add_suitcase(self, suitcase: Suitcase):
        total_weight = self.weight() + suitcase.weight()
        if total_weight <= self.max_weight:
            self.suitcases.append(suitcase)

    def weight(self):
        total = 0
        for suitcase in self.suitcases:
            total += suitcase.weight()
        return total

    def __str__(self):
        print_result = ""
        if len(self.suitcases) == 1:
            print_result += (f"{len(self.suitcases)} suitcase, space for "
                             f"{self.max_weight - self.weight()} kg")
        else:
            print_result += (f"{len(self.suitcases)} suitcases, space for "
                             f"{self.max_weight - self.weight()} kg")
        return print_result

    def print_items(self):
        for suitcase in self.suitcases:
            suitcase.print_items()


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)
    
    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)
    
    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)
    
    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
