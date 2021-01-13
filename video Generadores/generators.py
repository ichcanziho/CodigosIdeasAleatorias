import random
import time
import memory_profiler as mem_profile
import argparse


class Person:
    def __init__(self, identifier, name, age):
        self.name = name
        self.age = age
        self.id = identifier


def person_list(n, names_, ages_) -> list:
    """generates a list of persons with a random name and random age

        n-> int: number of persons to be generated
        names_ -> list: list with possible names
        ages_ -> list: list with possible ages

    """

    persons = []
    for i in range(n):
        persons.append(Person(i, random.choice(names_), random.choice(ages_)))
    return persons


def person_gen(n, names_, ages_) -> range:
    """yields an object from the class person, with a random name and random age

        n-> int: number of persons to be generated
        names_ -> list: list with possible names
        ages_ -> list: list with possible ages

    """

    for i in range(n):
        yield Person(i, random.choice(names_), random.choice(ages_))


def main(number_of_persons_, names_, ages_, choice_="queue"):
    """measures the time and memory to make 'number_of_persons' with a traditional method and with generators

        number_of_persons-> int: number of persons to be generated
        names_ -> list: list with possible names
        ages_ -> list: list with possible ages
        choice -> str: string for select the method to generate the objects from class Person ["queue", "other"]

    """

    print()
    print("------------")
    print("the method selected was:", choice)
    print("------------")
    print()

    print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB')
    t1 = time.time()
    if choice_ == "queue":
        people = person_list(number_of_persons_, names_, ages_)
    else:
        people = person_gen(number_of_persons_, names_, ages_)
    t2 = time.time()

    print('Memory (After) : ' + str(mem_profile.memory_usage()) + 'MB')
    print('Took {} Seconds'.format(t2-t1))

    for i in range(10):
        if choice == "queue":
            print(people[i])
        else:
            print(next(people))


def make_parser():
    """ Simple command line interface """
    parser = argparse.ArgumentParser(description="comparison between generators and lists")

    parser.add_argument("--objects", "-o", action="store", type=int, required=False,
                        help='the number of objects to be generated: 1000')
    parser.add_argument("--names", "-n", action="store", type=str, required=False,
                        help='list with possible names: "Gabriel Pedro"')
    parser.add_argument("--ages", "-a", action="store", type=str, required=False,
                        help='list with possible ages: "23 21"')
    parser.add_argument("--choice", "-c", action="store", type=str, required=False,
                        help='could be "choice" or "other"')
    args = parser.parse_args()
    if args.objects is None:
        nop = 1000000
    else:
        nop = args.objects
    if args.names is None:
        names = ['gab', 'juan', 'luis', 'alan', 'jorge', 'ale', 'kevin']
    else:
        names = args.names.split()
    if args.ages is None:
        ages = [23, 22, 19, 24, 26, 19, 29]
    else:
        ages = args.ages.split()
    if args.choice is None:
        choice = "queue"
    else:
        choice = args.choice
    print("your parameters are:")
    print("number of objects:", nop)
    print("names:", names)
    print("ages:", ages)
    print("choice:", choice)

    print()
    print("starting...")
    print()
    time.sleep(1)
    return nop, names, ages, choice


if __name__ == "__main__":
    nop, names, ages, choice = make_parser()
    main(number_of_persons_=nop, names_=names, ages_=ages, choice_=choice)
