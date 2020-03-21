"""
2. Задача полягає у вивченні і реалізації алгоритмів пошуку для даних, підготовлених
за допомогою функції моделювання випадкових чисел і текстів, підготовлених
самостійно.
2)бінарний пошук;
Barbak Vladuslav 122V
"""
import numpy as np  # Імпортуємо бібліотеку NumPy
import random  # Імпортуємо бібліотеку Random
while True: # Цикл створений для запуску програми з початку
    mas1=np.array(range(1,11))  # Створюємо масив, для перевірки правильності нашого пошуку.
    print(mas1)  # Виводемо створений масив
    x=int(input('Enter the item we are looking for '))  # Якщо користувач ввдед більше 10, то пошук не буде здійснено
    R=len(mas1)-1  # Кінець масиву
    L,count,k=0,0,0,  # Початок масиву, лічильник для порівнянь, і змінна для позиції числа
    flag=False
    while L<=R and not flag :
        k=(L+R)//2  # Припустимо, якщо ввести 9, При першій ітерації, к = 6, при другій к = 10 при третій к = 8
        count+=1   # Лічильник кожної дії
        if mas1[k]==x:
            flag=True
        elif mas1[k]<x:
            L=k+1
            count+=1
        else:
            R=k-1
            count+=1
    if not flag:
        print('No item')
    else:
        print(f'Element found at position {k} for {count} comparisons.')
    """
    Работа с рандомними значениями
    """
    mas2 = np.zeros(10, dtype=int)
    for i in range(10):
        mas2[i] = random.randint(0, 10)
    mas2 = sorted(mas2)
    print(mas2)
    R1 = len(mas2) - 1  # Кінець масиву
    L1, count1, k1 = 0, 0, 0,  # Початок масиву, лічильник для порівнянь, і змінна для позиції числа
    flag1 = False
    while L1 <= R1 and not flag1:
        k1 = (L1 + R1) // 2
        count1 += 1
        if mas2[k1] == x:
            flag1 = True
        elif mas2[k1] < x:
            L1 = k1 + 1
            count1 += 1
        else:
            R1 = k1 - 1
            count1 += 1  # Кількість зрівнянь
    if not flag1:
        print('No item')
    else:
        print(f'Element found at position {k1} for {count1} comparisons.')
    result = input('Want to restart? If yes - 1, No - other: ')  # Просимо користуввача ввести 1- для запуску з початку
    if result == '1':  # Якщо введене користувачем дорівнює 1, то код запускається з початку
        continue
    else:  # Інакше код завершується
        break
