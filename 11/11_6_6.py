# В рамках разработки шахматного ИИ стоит новая задача:
# по заданным вещественным координатам коня и точки программа должна определить,
# может ли конь ходить в эту точку.
# Используйте как можно меньше конструкций if и логических операторов. Обеспечьте контроль ввода.
print('Введите местоположение коня:')
x_coord = float(input("X: "))
y_coord = float(input("Y: "))
print('Введите местоположение точки на доске:')
point_x = float(input('X: '))
point_y = float(input('Y: '))

if (0 < x_coord < 0.8 and 0 < y_coord < 0.8) or (0 < point_x < 0.8 and 0 < point_y < 0.8):
    hx_number = int(x_coord * 10)
    hy_number = int(y_coord * 10)
    px_number = int(point_x * 10)
    py_number = int(point_y * 10)
    print("Конь находится в клетке (", hx_number, ",", hy_number, ")")
    print("Точка находится в клетках (", px_number, ",", py_number, ")")
    if abs((hx_number - px_number) * (hy_number-py_number)) == 2:
        print("Да, конь может ходить в эту точку.")
    else:
        print("Нет, конь не может ходить в эту точку.")
else:
    print("Клетки с такой координатой не существует")