def product_or_sum(num1: float, num2: float):
    result = num1 * num2
    if result <= 1000:
        if int(result) == result:
            return int(result)

        return result

    if int(num1 + num2) == num1 + num2:
        return int(num1 + num2)

    return num1 + num2


num1 = float(input('Enter 1st number: '))
num2 = float(input('Enter 2nd number: '))

print(product_or_sum(num1, num2))
