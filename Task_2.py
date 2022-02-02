from random import uniform
import operator

print('Задание 2.')

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


lst = [uniform(0, 50) for i in range(5)]
print('Список до сортировки:', lst)


def Merge(lst, compare=operator.lt):
    n = 0
    if len(lst) < 2:
        return lst[:]
    else:
        if len(lst) % 2 == 0:
            while n < len(lst):
                middle = int(len(lst) / 2)
                left = Merge(lst[:middle], compare)
                right = Merge(lst[middle:], compare)
                n += 1
                return merge(left, right, compare)
        else:
            while n < len(lst):
                middle = int(len(lst) // 2)
                left = Merge(lst[:middle], compare)
                right = Merge(lst[middle:], compare)
                n += 1
                return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


merge_res = Merge(lst)
print('Список после сортировки:', merge_res)