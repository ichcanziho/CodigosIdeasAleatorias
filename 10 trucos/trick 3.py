import sys


def show_help():
    print("Este simple truco nos permite conocer \n"
          "el espacio de memoria que utiliza una \n"
          "variable en python :), muy útil para listas.\n"
          "-------------------------------------------")


if __name__ == "__main__":
    show_help()
    name = "Gabriel Ichcanziho"
    print(name)
    print(sys.getsizeof(name))
