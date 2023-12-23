nums = int(input("Введите кол-во чисел: "))
k = 0
count = 0
for x in range(nums):
  pars = int(input('Введите число: '))
  for i in range(2, pars // 2+1):
      if (pars % i == 0):
          k = k+1
  if (k <= 0):
      print("Число простое")
      count += 1
  else:
      k = 0
print("Количество простых чисел в последовательности: ", count)
