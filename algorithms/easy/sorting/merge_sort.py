
def merge_sort(arr):

    if(len(arr) <= 1):
        return arr

    mid = len(arr)//2

    a1 = arr[0:mid]
    a2 = arr[mid:]

    return merge(merge_sort(a1), merge_sort(a2))


def merge(a1, a2):

    total_length = len(a1)+len(a2)

    a1_index, a2_index = 0, 0

    result = []

    while len(result) < total_length:

        if a1_index == len(a1):
            result.append(a2[a2_index])
            a2_index += 1
        elif a2_index == len(a2):
            result.append(a1[a1_index])
            a1_index += 1
        else:
            if a1[a1_index] <= a2[a2_index]:
                result.append(a1[a1_index])
                a1_index += 1
            else:
                result.append(a2[a2_index])
                a2_index += 1

    return result


print(merge_sort([0, -1, 8]))
