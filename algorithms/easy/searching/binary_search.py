def binary_search(arr, element):

    start, mid, end = 0, 0, len(arr)-1

    while start <= end:

        mid = (start+end) // 2

        if arr[mid] == element:
            return True

        elif arr[mid] > element:
            end = mid-1

        else:
            start = mid+1

    return False


arr = [2, 4, 5, 6, 7, 8, 9, 15]

print(binary_search(arr, 2))
