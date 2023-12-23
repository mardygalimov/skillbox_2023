nums = int(input("Введите кол-во чисел: "))
ost_sum = 0
countNum = 0
itog = 0
buff = 0
for x in range(nums):
  line = int(input('Введите число: '))
  buff = line
  while line > 0:
      ostatok = line % 10
      ost_sum += ostatok
      line //= 10
  if itog <= ost_sum:
      itog = ost_sum
      ost_sum = 0
      itog_buff = buff
  else:
      ost_sum = 0
print("Сумма цифр числа ", itog)
print("Число: ", itog_buff)