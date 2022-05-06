def bubble_sort(arr):
    for i in range(3):
        for j in range(len(arr)-i-1):
            k = j+1
            if arr[j] > arr[k]:
                arr[j], arr[k] = arr[k], arr[j]

    return arr


print(bubble_sort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))
