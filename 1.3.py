"""
1. Напишіть програми, що виконують такі операції з масивами (використовувати
вбудовані методи по роботі з масивами заборонено):
3)виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
Результати множення елементів занесіть до нової матриці та виведіть її на екран;
Barbak Vladuslav 122V
"""
import numpy as np # Імпортуємо бібліотеку NumPy
q=0
w=[]  # Створюємо порожню змінну для запису результатів множення і 2 порожніх списки, що б додавати наші значення туди
e=[]
while True: # Цикл створений для запуску програми з початку
    n,p=int(input('Enter quantity rows 1 matrix:  ')),int(input('Enter quantity column 1 matrix: ')) # Вводемо розмірність 1 матриці
    v,x=int(input('Enter quantity rows 2 matrix:  ')),int(input('Enter quantity column 2 matrix: ')) # Вводемо розмірність 2 матриці
    while n !=3 and p !=3: # Перевірка на розмірність саме 3 на 3
        n, p = int(input('Enter quantity rows 1 matrix:  ')), int(input('Enter quantity column 1 matrix: '))
        v, x = int(input('Enter quantity rows 2 matrix:  ')), int(input('Enter quantity column 2 matrix: '))
    g=np.zeros((n,p),dtype=int) # Ініціалізуєм матрицю нулями, і прісваеіваем типу даних тип даних int
    h=np.zeros((v,x),dtype=int) # Ініціалізуєм матрицю нулями, і прісваеіваем типу даних тип даних int
    for i in range(n) : # Проходим ко кожному рядку 1 матриці
        for j in range(p): # Проходим ко кожному стовпцю 1 матриці
            g[i,j]=int(input(f'G[{i+1},{j+1}]=')) # Заповнюємо 1 матрицю значиннями
    print('First matrix')
    print(g)
    for o in range(v): # Проходим ко кожному рядку 2 матриці
        for z in range(x): # Проходим ко кожному стовпцю 2 матриці
            h[o,z]=int(input(f'H[{o+1},{z+1}]=')) # Заповнюємо 2 матрицю значиннями
    print('Second matrix')
    print(h)
    for i in range(n): # Проходим ко кожному рядку 1 матриці
            for z in range(x): # Проходим ко кожному стовпцю 2 матриці
                for j in range(p): # Проходим ко кожному стовпцю 1 матриці
                   q=q+g[i][j]*h[j][z] # Виконується множення матриць і результат запиуєтья в порожню змінну
                w.append(q) # добавим значние в список
                q=0 # переприсвоем значения к нулю
            e.append(w) # после расчета всех значений,записываем их в финальный список
            w=[]
    print(f' Third matrix ')
    print(e)
    result = input('Want to restart? If yes - 1, No - other: ')  # Просимо користуввача ввести 1- для запуску з початку
    if result == '1':  # Якщо введене користувачем дорівнює 1, то код запускається з початку
        continue
    else:  # Інакше код завершується
        break

