cost_eur = int(input("Введите стоимость покупки в Евро: "))

cost_rubls = (cost_eur * 1.25) * 60.87
print("Стоимость покупки в рублях: ", round(cost_rubls, 2))