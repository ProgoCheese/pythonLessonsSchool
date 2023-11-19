def shaker_sort(array):
    swapped = True
    start_index = 0
    end_index = len(array) - 1

    while swapped:
        swapped = False

        # проход слева направо
        for i in range(start_index, end_index):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if (not (swapped)):
            break

        swapped = False
        end_index = end_index - 1

        # проход справа налево
        for i in range(end_index - 1, start_index - 1, -1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        start_index = start_index + 1


user_list = input().split()
shaker_sort(user_list)
print("Отсортированный массив: ")
print(user_list)