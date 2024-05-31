# Алгоритм сортировки выбором. Сортировка массива по возрастанию
def find_smallest(arr): # Функция нахождения наименьшего элемента массива
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr): # Функция сортировки выбором. Время выполнения On^2
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print (selection_sort([5, 3, 6, 2, 10]))