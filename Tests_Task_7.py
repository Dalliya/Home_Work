#Найти сумму десяти первых чисел ряда Фибоначчи.

numbers = []

def fabionachi(numbers):
    numbers = [1,1]
    i = 2
    while True:
        numbers.append(numbers[i-1] + numbers[i-2])
        if i >= 10:
            del numbers[i]
            break
        else:
            i += 1
    sum_total = sum(numbers)
    return sum_total

print(fabionachi(numbers))

