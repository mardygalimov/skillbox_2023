# Саша просыпается когда угодно, но в 23 часа уже точно идёт спать.
# Питается Саша следующим образом: каждые 3 часа он выпивает литр воды и съедает N калорий.
# Пить и есть он, кстати, начинает сразу как только проснётся.
# Напишите программу, которая считает сколько он выпьет литров воды и сколько калорий он съест
# перед тем как пойдёт спать.
calories = 0
wakeup = int(input('Во сколько проснулся: '))
water= 0
calories_summ = 0
for hour in range(wakeup, 23, 3):
    print("Нужно поесть")
    water += 1
    calories = int(input("Сколько сЪел калорий: "))
    calories_summ += calories
print('Выпито воды: ', water)
print('Съедено калорий: ', calories_summ)