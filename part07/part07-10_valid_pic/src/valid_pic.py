# Write your solution here

from datetime import datetime

def is_it_valid(pic: str) -> bool:
    if len(pic) != 11:
        return False

    try:
        dd = pic[:2]
        mm = pic[2:4]
        yy = pic[4:6]
        X = pic[6]
        yyy = pic[7:10]
        z = pic[10]

        if int(dd) < 1 or int(dd) > 31:
            return False
        if int(mm) < 1 or int(mm) > 12:
            return False
        if int(yy) < 1800 and int(yy) > 2999:
            return False
        if X not in ["-", "+", "A"]:
            return False
        if z != "0123456789ABCDEFHJKLMNPRSTUVWXY"[int(dd + mm + yy + yyy) % 31]:
            return False

        if X == "+":
            century = 1800
        if X == "-":
            century = 1900
        if X == "A":
            century = 2000
            
        date = datetime(int(yy) + century, int(mm), int(dd))
        
        return True
    except:
        return False

if __name__ == "__main__":
    print(is_it_valid("081142-720N"))
