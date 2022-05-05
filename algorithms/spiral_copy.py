def spiral_copy(my_arr):
    '''Just keeping a track of the coordinates is the main thing'''

    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

    length = len(my_arr)
    breath = len(my_arr[0])
    top, bottom, left, right = 0, length-1, 0, breath-1
    result = []
    turn = RIGHT

    while(len(result) != length*breath):

        if turn == RIGHT:
            for i in range(left, right+1):
                result.append(my_arr[top][i])
            top += 1
        elif turn == DOWN:
            for i in range(top, bottom+1):
                result.append(my_arr[i][right])
            right -= 1
        elif turn == LEFT:
            for i in range(right, left-1, -1):
                result.append(my_arr[right][i])
            bottom -= 1
        elif turn == UP:
            for i in range(bottom, top-1, -1):
                result.append(my_arr[i][left])
            left += 1

        turn += 1
        turn %= 4

    return result


    # left             #right
arr = [[1, 2, 3, 4, 5],  # top
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20]]  # bottom

print(spiral_copy(arr))

assert (spiral_copy([[]]) == [])
assert (spiral_copy([[2, 3]]) == [2, 3])
assert (spiral_copy([[2, 3, 4], [5, 8, 9]]) == [2, 3, 4, 9, 8, 5])
