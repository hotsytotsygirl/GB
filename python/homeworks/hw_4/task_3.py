# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.


lst = [1, 8, 8, 8, 5, 4, 2, 3]
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(f'исходный список: {lst}, новый список: {new_lst}')