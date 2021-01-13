import random
import time
import memory_profiler as mem_profile


class Person:
    def __init__(self, identifier, name, age):
        self.name = name
        self.age = age
        self.id = identifier


def person_list(n, names_, ages_):

    persons = []
    for i in range(n):
        persons.append(Person(i, random.choice(names_), random.choice(ages_)))
    return persons


def person_gen(n, names_, ages_):

    for i in range(n):
        yield Person(i, random.choice(names_), random.choice(ages_))


def main(number_of_persons_, names_, ages_, choice_="queue"):

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


if __name__ == "__main__":
    nop = 1000000
    names = ['gab', 'juan', 'luis', 'alan', 'jorge', 'ale', 'kevin']
    ages = [23, 22, 19, 24, 26, 19, 29]
    choice = "gen"
    main(number_of_persons_=nop, names_=names, ages_=ages, choice_=choice)
