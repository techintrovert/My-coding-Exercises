def max_numbers(a, b):
    max = 0
    if a > b:
        max = a
        return max
    else:
        max = b
        return max


a = int(input("Enter a: "))
b = int(input("Enter b: "))
maximum = max_numbers(a ,b)
print(maximum)