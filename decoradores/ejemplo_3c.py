class AnimalClass:

    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name, "loves to walk")
        print("---------")


class Decorators:
    @classmethod
    def change_walk(cls, decorated, msg):
        print(msg)
        return decorated


class SeaAnimal(AnimalClass):

    def __init__(self, name):
        super(SeaAnimal, self).__init__(name)
        self.walk = Decorators.change_walk(self.walk, "Using their fins")


class EarthAnimal(AnimalClass):

    def __init__(self, name):
        super(EarthAnimal, self).__init__(name)
        self.walk = Decorators.change_walk(self.walk, "Using their legs")


if __name__ == '__main__':

    base_animal = AnimalClass("Juan")
    base_animal.walk()
    sea_animal = SeaAnimal("Alan")
    sea_animal.walk()
    earth_animal = EarthAnimal("Gabriel")
    earth_animal.walk()

