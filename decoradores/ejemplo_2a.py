
# we can construct a simple decorator function with unknown parameters as follows:
def greeting_function(function):
    def decorator(*args, **kwargs):
        print("Hello World!")
        return function(*args, **kwargs)
    return decorator


@greeting_function
def get_int_division(a, b):
    return a // b


if __name__ == '__main__':

    print("outer ans:", get_int_division(5, 2))
