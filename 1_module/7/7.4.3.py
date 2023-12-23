wake_up = int(input('Во сколько ты проснулся? '))
callories = 0
total_call = 0
hours = 0
for hour in range(wake_up,23):
    print("Сейчас", hour, "часов")
    callories = int(input('Сколько ты съел калорий? '))
    total_call += callories
    hours += 1
    if total_call > 2000:
        print('Хорошо поели, теперь можно и поспать')
        break
print('Всего съел калорий ', total_call)
print('Часов бодрствовал ', hours)