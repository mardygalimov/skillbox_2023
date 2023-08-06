for num in range(10,100):
    dec = num % 10
    edins = num // 10
    if (3 * dec * edins) == num:
        print(num)