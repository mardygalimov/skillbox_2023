# Напишите программу, которая получает на вход начало и конец отрезка,
# а также шаг (отрицательный), а затем высчитывает функцию
# y в каждой точке отрезка и выводит ответ на экран с нужным шагом, начиная с конца.
# y = x**3+2*x**2-4*x+1
start = int(input('Введите начало отрезка: '))
end = int(input('Введите конец отрезка: '))
step = int(input('Введите шаг: '))
if start < 0 and end < 0:
#OK
      if start < end:
            a = start
            b = end
            c = step
#OK
      else:
            a = end
            b = start
            c = step
      for x in range(b, a-1, c):
          print('В точке', x, 'функция равна ', ((x ** 3) + (2 * (x ** 2)) - (4 * x) + 1))
elif start > 0 and end > 0:
      if start < end:
           a = start
           b = end
           c = step
#OK
      else:
          a = end
          b = start
          c = step
      for x in range(b, a-1, c):
          print('В точке', x, 'функция равна ', ((x ** 3) + (2 * (x ** 2)) - (4 * x) + 1))
#OK
elif start > 0 > end:
     a = start
     b = end
     c = step*(-1)
     for x in range(b, a+1, c):
       print('В точке', x, 'функция равна ', ((x ** 3) + (2 * (x ** 2)) - (4 * x) + 1))
#OK
elif end > 0 > start:
    a = end
    b = start
    c = step
    for x in range(a, b-1, c):
       print('В точке', x, 'функция равна ', ((x**3)+(2*(x**2))-(4*x)+1))
