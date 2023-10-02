people = int(input('Введите колчиество людей в очереди: '))
for hours in range(people+1):
    print('Идет час: ', hours)
    for num in range(hours, people):
        print('Номер в очереди: ',num)
    print()
print('Обслуживание очереди законченно')