def is_primal(number: int):
    if number < 0:
        raise ValueError("Not Negative")

    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def minimum(*args: int) -> int:
    result = args[0]
    for arg in args:
        if arg <= result:
            result = arg

    return result


# minimum(1,2,3,4,5)
# print(is_primal(1))
