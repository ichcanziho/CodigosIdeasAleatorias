
# lets make our first decorator a function that
# modify the original behavior of a given input function
def catch_zero_denominator(function):  # HINT: this is the WRAPPER function NAME
    """
    this is a simple decorator function, that checks ir a denominator of a division
    is equals to 0
    :param function: a reference to a function NOT a instance of a function
    :return: the same input function, but with additional behavior.
    """
    def decorator(a, b):  # HINT: this is the decorator behavior
        if b != 0:
            return function(a, b)  # I return the original function if the denominator is different to 0
        else:
            return -1  # Otherwise I return -1
    return decorator


# this is the pythonize way to do the same of the last example
@catch_zero_denominator
def get_module_division(a, b):
    return a % b


@catch_zero_denominator
def get_int_division(a, b):
    return a // b


if __name__ == '__main__':

    print(get_module_division(5, 0))
    print(get_int_division(5, 0))
