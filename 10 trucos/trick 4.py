def show_help():
    print("Con este truco podemos conocer los  \n"
          "métodos y atributos de una clase. \n"
          "-------------------------------------------")


if __name__ == "__main__":
    show_help()
    python_object = range
    for method in dir(python_object):
        print(method)
