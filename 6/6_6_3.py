num = int(input('Введите число: '))
count = 0
while num >= 0:
    num = num // 10
    count += 1
    if num == 0:
        break
print(count)
