def bubble_sort(arr):

    for f in range(len(arr)):
        for l in range(f+1, len(arr)):
            if arr[f] > arr[l]:
                arr[f], arr[l] = arr[l], arr[f]


arr = [0, -1]

bubble_sort(arr)

print(arr)
