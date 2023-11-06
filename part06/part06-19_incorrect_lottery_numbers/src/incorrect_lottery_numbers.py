# Write your solution here

def valid_lotteries(lotteries: str) -> bool:
    lottery_list = lotteries.split(",")
    if len(lottery_list) != 7:
        return False
    for lottery in lottery_list:
        try:
            lottery = int(lottery)
            if lottery_list.count(str(lottery)) > 1:
                return False
            if lottery < 1 or lottery > 39:
                return False
        except:
            return False
    return True

def valid_week(week: str) -> bool:
    try:
        week = int(week)
    except:
        return False
    return True

def filter_incorrect():
    try:
        with open("lottery_numbers.csv") as lottery_file:
            with open("correct_numbers.csv", "w") as correct_file:
                for line in lottery_file:
                    line = line.strip()
                    parts = line.split(";")
                    week = parts[0].split(" ")[1]
                    lotteries = parts[1]
                    if valid_week(week) and valid_lotteries(lotteries):
                        correct_file.write(line+"\n")
    except:
        print("Unable to open lottery_numbers.csv")

