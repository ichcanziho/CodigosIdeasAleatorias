def show_help():
    print("Con este truco podemos ver una barra\n"
          "de progreso en nuestros cliclos for.\n"
          "en una terminal escribir: pip install tqdm\n"
          "---------------------------------------")


def show_progress_bar(n=10):
    from tqdm import tqdm
    from time import sleep
    for _ in tqdm(range(n)):
        sleep(0.5)


if __name__ == "__main__":
    show_help()
    show_progress_bar()
