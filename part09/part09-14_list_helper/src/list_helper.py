# WRITE YOUR SOLUTION HERE:

class ListHelper:
    my_dict = {}

    def greatest_frequency(my_list: list):
        my_dict = {}
        for item in my_list:
            if item not in my_dict:
                my_dict[item] = 1
            else:
                my_dict[item] += 1
        most_common_freq = 0
        most_common_item = 0
        for number, count in my_dict.items():
            if count > most_common_freq:
                most_common_freq = count
                most_common_item = number
        return most_common_item

    def doubles(my_list: list):
        my_dict = {}
        for item in my_list:
            if item not in my_dict:
                my_dict[item] = 1
            else:
                my_dict[item] += 1
        unique_items = []
        for item, count in my_dict.items():
            if count >= 2:
                unique_items.append(item)
        return len(unique_items)


if __name__ == "__main__":
    numbers = [1, 1, 1, 2, 2, 3]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
