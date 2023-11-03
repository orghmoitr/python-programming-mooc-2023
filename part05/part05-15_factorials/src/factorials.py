# Write your solution here

def factorials(n: int) -> dict:
    fact = {}
    for i in range(1, n+1):
        product = 1
        j = 1
        while j <= i:
            product *= j
            j += 1
        fact[i] = product
        i += 1
    return fact
    

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])    
