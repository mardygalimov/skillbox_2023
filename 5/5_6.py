s = int(input('Введите площадь квартиры:'))
price = int(input('Введите цену:'))
if (s > 80 and s < 100) and price >= 7000000:
    print('Квартира меньше 100м, но цена меньше 7млн - подходит')
elif s >= 100 and price <= 1000000:
    print('Квартира не меньше 100м, цена меньше 10млн  - подходит')
else:
    print('Квартира не подходит')