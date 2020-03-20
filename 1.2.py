"""
1. Напишіть програми, що виконують такі операції з масивами (використовувати
вбудовані методи по роботі з масивами заборонено):
2)виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана
користувачем).
Barbak Vladuslav 122V
"""
import numpy as np # Імпортуємо бібліотеку NumPy
while True: # Цикл створений для запуску програми з початку
    n=int(input('Enter quantity rows:  ')) # Вводемо розмірність матриці
    p=int(input('Enter quantity column: ')) # Вводемо розмірність матриці
    while n!=3 and p!=3: # Перевірка на розмірність саме 3 на 3
        n = int(input('Enter quantity rows:  '))
        p = int(input('Enter quantity column: '))
    a=np.zeros((n,p),dtype=int) # Ініціалізуєм матрицю нулями, і прісваеіваем типу даних тип даних int
    for i in range(n): # import numpy as np # Імпортуємо бібліотеку NumPy ко кожному рядку
        for j in range(p): # Проходим ко кожному стовпцю
            a[j,i]=int(input(f'A[{i+1},{j+1}]=')) # Заповнюємо матрицю значиннями і зразу троанспонуєм її
    print('The transposed matrix',a)
    result = input('Want to restart? If yes - 1, No - other: ')  # Просимо користуввача ввести 1- для запуску з початку
    if result == '1':  # Якщо введене користувачем дорівнює 1, то код запускається з початку
        continue
    else:  # Інакше код завершується
        break
