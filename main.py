# Module 2 Practice HARD
import time

print('Введите целое число от 3 до 20, для определения пароля')
number = int(input())
password = []
if 3 <= number <= 20:
    print('Работаем...')
    for i in range (1, number):
        number % i == 0
        for j in range (1, number):
            number % j == 0
            if number % (i + j) == 0 and i != j and i < j:
                password.append(i)
                password.append(j)
            else:
                continue
    time.sleep(1)
    print('Пароль: ', *password)
else:
    print('Введено неверное число')

#   a * b = c
#   number % a == 0 and number % b == 0