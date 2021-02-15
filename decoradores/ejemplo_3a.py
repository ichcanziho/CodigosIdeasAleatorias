# we can even make decorators using Classes instead of functions
class MyClassDecorator(object):
    def __init__(self, function):
        print("I have constructed a new class")
        self.function = function

    def __call__(self, *args, **kargs):  # we defined as "CALLABLE"
        print("I'm a method called using __call__ magic method")
        self.function(*args, **kargs)


@MyClassDecorator
def speak(*args):
    for msg in args:
        print(msg)


if __name__ == '__main__':

    speak("Subscribe to my CHANNEL", "Ideas Aleatorias :D")
