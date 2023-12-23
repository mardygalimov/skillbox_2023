number = float(input("Введите число:" ))
count = 0
while number > 10:
    number = number / 10
    count += 1
print("Формат плавающей точки: x= ", float(number), "* 10 ", "**", count)