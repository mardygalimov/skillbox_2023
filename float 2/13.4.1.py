def nalog (tax, new_tax):
    print("tax=", tax)
    print("new_tax=", new_tax)
    summ = tax + new_tax
    if abs(summ - tax) <= 1e-15 or abs(summ - new_tax) <= 1e-15:
        print("Результат: Бюджет не изменится")
    else:
        print("Результат: Бюджет увеличится")

tax = float(input("Введите бюджет страны: " ))
new_tax = float(input("Новые поступления (налог): " ))
nalog(tax, new_tax)