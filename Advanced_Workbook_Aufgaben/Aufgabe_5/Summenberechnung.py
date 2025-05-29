class Summenberechnung:
    pass

def summe(n):
    if n == 0:
        return 0
    else:
        return n + summe(n - 1)

if __name__ == "__main__":
    n = 5
    print(summe(n))

#summe(5)
#5 + 4 + 3 + 2 + 1 + 0 = 15
