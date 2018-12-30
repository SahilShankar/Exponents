def power_of_number(base, exponent):
    product = 1
    for i in range(exponent):
        product = product * base
    return product


base = int(input("Enter a base: "))
exponent = int(input("Enter an exponent: "))
print(power_of_number(base,exponent))
