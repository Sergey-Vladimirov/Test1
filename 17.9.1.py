array = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
element = int(input('Ввведите любое число: '))
while element:
    if element <= min(array):
        print('Введённое число не соответствует критериям поиска, введите число не превышающее максимальное значение и'
              ' больше минимального')
        element = int(input('Ввведите любое число: '))
    elif element > max(array):
        print('Введённое число не соответствует критериям поиска, введите число не превышающее максимальное значение и'
              ' больше минимального')
        element = int(input('Ввведите любое число: '))
    else:
        break

def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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

print(merge_sort(array))

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle-1)
    else:
        return binary_search(array, element, right, middle+1)

print(binary_search(array, element, 0,  len(array)))