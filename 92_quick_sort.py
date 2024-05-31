def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot] # Подмассив всех элементов меньше опорного
        greater = [i for i in array[1:] if i > pivot] # Подмассив всех элементов больше опорного
        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([12, 45, 2, 78, 10, 9, 14, 1]))