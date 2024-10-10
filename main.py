#Дополнительное практическое задание по модулю: "Основные операторы"

def number_pair(n):
    result = ""              #  Создадим пустую строку, в которую буду добавлять пары после каждой итерации цикла
    for i in range(1, n):    # При помощи цикла for перебираем список для первого числа пары
        for j in range(i + 1, n):   # перебираем список для второго числа пары при этом исключаем число равное i
            if n % (i + j) == 0:    # проверяем делится ли число n на сумму чисел i и j без остатка
                result += str(i) + str(j)  # если делится, то нашли нужную пару и ищем следующую, если она есть
    return result

print('Введите число: ')
print(number_pair(int(input())))
