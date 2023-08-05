N = (100+1) //2
low = 1
high = 100
while True:
    print('Твое число равно, больше или меньше числа', N, '?')
    answer = int(input('1 - равно, 2 - больше, 3 - меньше:'))
    if answer == 1:
        print('Я угадал!')
        break
    elif answer == 2:
        low = (N+1) #51
        N = (N+high+1)//2 #75
    else:
        high = (N-1) #74
        N = (low+high+1) //2