summ_empl = int(input("Кол-во сотрудников в офисе: "))
empl_ID = []
id = 0
ID_search = 0
work = 0
for _ in range(summ_empl):
    id = int(input("ID сотрудника: "))
    empl_ID.append(id)
print(empl_ID)

ID_search = int(input("Какой ID ищем? "))


if ID_search not in empl_ID:  # Благодаря оператору in поиск можно упростить
    print("Сотрудник не работает!")
else:
    print("Сотрудник работает!")