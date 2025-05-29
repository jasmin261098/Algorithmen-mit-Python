class EvenNumbers:
    pass

def even_number_counter(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0: 
            count += 1
    return count

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    print(even_number_counter(numbers))

#Anzahl an geraden Zahlen: 3