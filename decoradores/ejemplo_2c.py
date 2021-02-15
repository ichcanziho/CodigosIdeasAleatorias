
def greeting_function(function):
    def decorator(*args, **kwargs):
        print("Hello World!")
        return function(*args, **kwargs)
    return decorator


def goodbye_function(message):
    """
    message is a parameter of the over decorator, not of the inner decorator
    :param message: a goodbye message
    :return: a function decorated
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            answer = function(*args, **kwargs)
            print("the results is:", answer)
            print(message)
            return answer
        return wrapper
    return decorator


@greeting_function
@goodbye_function(message="see you soon!")
def get_int_division(a, b):
    return a // b


if __name__ == '__main__':

    print("outer ans:", get_int_division(5, 2))
