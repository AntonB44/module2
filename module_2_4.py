'''Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
Цель: закрепить навык решения задач при помощи цикла for, применив знания
об основных типах данных.
Задача "Всё не так уж просто":'''
'''Создайте пустые списки primes и not_primes.
При помощи цикла for переберите список numbers.
Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes
в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
Выведите списки primes и not_primes на экран(в консоль).'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes =[]# Объявляем пустой список простых чисел
not_primes =[]# Объявляем пустой список не простых чисел и начинаем проверку делимости, выполняя рекомендации задачи.
for i in range(len(numbers)):
    is_prime = True
    for j in range(2,numbers[i] - 1):
        if numbers[i] % j == 0:
            is_prime = False
            break
        else:
            continue
    if is_prime and numbers[i] == 1:
        print('Единица исключается')
    elif is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print(f'Primes:{primes}')
print(f'Not_Primes:{not_primes}')



