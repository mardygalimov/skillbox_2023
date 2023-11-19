def count_numbers(temp):
    num_count = 0
    while temp > 0:
        num_count += 1
        temp = temp // 10
    return num_count
#    print("Кол-во цифр в числе: ", num_count)

def change_number(first_n):
    first_num_count = count_numbers(first_n)
    last_digit = first_n % 10
    first_digit = first_n // 10 ** (first_num_count - 1)
    between_digits = first_n % 10 ** (first_num_count - 1) // 10
    first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
    return first_n
#    print('Изменённое число:', first_n)

def main():
    x = int(input("Введите x - первое число: "))
    y = int(input("Введите y - второе число: "))
    c_n_x = count_numbers(x)
    c_n_y = count_numbers(y)
    if  c_n_x < 3:
        print("Во первом числе меньше 3х цифр.")
    elif c_n_y < 4:
        print("Во втором числе меньше 4х цифр.")
    else:
        print("Измененное первое число:", change_number(x))
        print("Измененное второе число:", change_number(y))
    print('\nСумма чисел:', change_number(x) + change_number(y))

#n = int(input("Введите число: "))
#count_numbers(n)

#change_number(n)
main()