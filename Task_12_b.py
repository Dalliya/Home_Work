number = input()

def sum_of_digits(number):
    result = int(number) // 100 + int(number) % 100 // 10 + int(number) % 10
    return result

result = sum_of_digits(number)
print(result)
