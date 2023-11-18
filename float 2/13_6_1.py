number = float(input("Введите число:" ))
count = 0
if number < 1.0:
    #print(number)
    while number < 1.0:
        number = number * 10
        #print(number)
        count -= 1
        #print("Формат плавающей точки: x=", float(number), "* 10 ", "**", count)
        #break
    print("Формат плавающей точки: x=", round(number,1), "* 10 ", "**", count)
else:
    while number > 10:
        number = number / 10
        count += 1
    print("Формат плавающей точки: x= ", float(number), "* 10 ", "**", count)