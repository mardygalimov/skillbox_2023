string = input('Введите строку:')
numm = 0
for symbol in string:
	if symbol != "*":
		numm += 1
	else:
		numm += 1
		break
print("* стоит на ", numm, "позиции")