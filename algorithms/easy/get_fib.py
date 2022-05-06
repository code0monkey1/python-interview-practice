
dict = {

}


def get_fib(position):
    if position <= 1:
        return position
    return get_fib(position-1)+get_fib(position-2)


'''Iterative version of get_fib'''


def i_get_fib(position):

    if position <= 1:
        return position

    first = 0
    second = 1

    next = first + second

    for _ in range(2, position):
        first, second = second, next
        next = first + second

    return next


print(get_fib(8))
