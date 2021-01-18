def show_help():
    print("Este truco nos permite juntar/unir/fusionar  \n"
          "dos diccionarios diferentes en python. \n"
          "-------------------------------------------")


if __name__ == "__main__":
    show_help()
    dic_1 = {"Gabriel": 23,
             "Pepe": 24}

    dic_2 = {"Tavo": 20,
             "Alan": 25}

    dic_3 = {**dic_1, **dic_2}

    print(dic_3)
