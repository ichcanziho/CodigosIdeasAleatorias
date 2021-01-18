def show_help():
    print("Con este pequeño truco puedes recorrer \n"
          "varios elementos de listas diferentes \n"
          "al mismo tiempo y de forma muy legible.\n"
          "----------------------------------------")


def show_multiple_lists_elements_traditional(list_1=("Gabriel", "Pepe", "Juan"), list_2=(23, 22, 24)):

    for i in range(len(list_1)):
        print(list_1[i], list_2[i])


def show_multiple_lists_elements_trick(list_1=("Gabriel", "Pepe", "Juan"), list_2=(23, 22, 24)):

    for name, age in zip(list_1, list_2):
        print(name, age)


if __name__ == "__main__":
    show_help()
    show_multiple_lists_elements_traditional()
    print("--------")
    show_multiple_lists_elements_trick()