#2. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

inpt = [1.1, 1.2, 3.1, 5, 10.01]

def find_sub(input: list):
    maximum = max(map(lambda x: x%1 ,filter(lambda x: x % 1 != 0, input)))
    minimum = min(map(lambda x: x%1 ,filter(lambda x: x % 1 != 0, input)))
    return round(maximum - minimum,2)

print(find_sub(inpt))
