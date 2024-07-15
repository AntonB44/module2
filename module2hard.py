'''Дополнительное практическое задание по модулю: "Основные операторы"
Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
Я реализовал следующий алгоритм:
Заданному числу n будет генерироваться пароль функцией password(n)
Для этого понадопится вспомогательная функция number_in_pairs(m) которая выводит для заданного числа комбинацию уникальных
пар. Вызываем эту функцию при каждом заданном числе из первой вставки и уникальному кратному к нему'''


def password(n):
    def number_in_pairs(m):
        num_1 = ""
        if m % 2 == 0:
            for i in range(1, m // 2):
                num_1 = num_1 + str(i) + str(m - i)
        else:
            for j in range(1, m // 2 + 1):
                num_1 = num_1 + str(j) + str(m - j)
        return num_1
    pass_1 = ""
    pass_mult = ""
    pass_1 = number_in_pairs(n)
    for k in range(2, n):
        if n % k == 0:
            pass_mult = pass_mult + number_in_pairs(k)
        else:
            continue
    return pass_mult + pass_1


for i in range(3,21):
    result_i = password(i)
    print(f'{i}-{result_i}')