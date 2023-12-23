# Известно, что амплитуда качающегося маятника с каждым разом затухает на 8,4% от амплитуды предыдущего колебания.
# Если качнуть маятник, то, строго говоря, он не остановится никогда,
# просто амплитуда будет постоянно уменьшаться до тех пор, пока мы не сочтём такой маятник остановившимся.
# Напишите программу, определяющую, сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится.
#
# Программа получает на вход начальную амплитуду колебания в сантиметрах и конечную амплитуду колебаний,
# которая считается остановкой маятника. Обеспечьте контроль ввода.

while True:
    attenuation_amplitude = 8.4 / 100
    amplitude = int(input("Введите начальную амплитуду: "))
    amplitude_stop = float(input("Введите амплитуду остановки: "))
    count = 0

    if amplitude <= 0 or amplitude_stop <= 0 or attenuation_amplitude <= 0:
        print("\nОшибка ввода данных. Попробуйте еще раз! \n")
    else:
        while amplitude > amplitude_stop:
            amplitude *= 1 - attenuation_amplitude
            count += 1

        print(f"\nМаятник считается остановившимся через {count} колебаний\n")