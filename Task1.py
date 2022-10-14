# 1. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]
import random

random_list = [random.randint(1,20) for i in range(1,1+int(input('Введите длину списка: ')))]
new_list = [random_list[i] + random_list[-(i+1)] for i in range(0,(len(random_list)+1)//2)]
print(random_list)
print(new_list)
