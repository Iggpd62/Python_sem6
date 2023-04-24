# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).

lst = list(map(int, input().split()))
minimum = int(input())
maximum = int(input())

indices = [i for i in range(len(lst)) if lst[i] >= minimum and lst[i] <= maximum]
result = ", ".join(f"{i}({lst[i]})" for i in indices)

print(result)