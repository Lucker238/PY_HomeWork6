#3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

def create_list(N):
    rand_list = [0] * N
    rand_list = list(map(lambda x: x + random.randint(1,10), rand_list))
    return rand_list

def sorted_list(some_list):
    result = list(filter(lambda x: some_list.count(x) == 1, some_list))
    return result

random_list = create_list(int(input("Введите длину списка: ")))
print(random_list)
print(sorted_list(random_list))