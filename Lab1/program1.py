def product_or_sum(num1: float, num2: float):
    result = num1 * num2
    if result <= 1000:
        return result

    return num1 + num2


num1 = float(input('Enter 1st number: '))
num2 = float(input('Enter 2nd number: '))

print(product_or_sum(num1, num2))
