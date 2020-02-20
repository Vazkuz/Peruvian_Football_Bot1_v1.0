import facebook
import itertools
import random


def make_day(num_teams, day):
    # using circle algorithm, https://en.wikipedia.org/wiki/Round-robin_tournament#Scheduling_algorithm
    assert not num_teams % 2, "Number of teams must be even!"
    # generate list of teams
    lst = list(range(1, num_teams + 1))
    # rotate
    day %= (num_teams - 1)  # clip to 0 .. num_teams - 2
    if day:                 # if day == 0, no rotation is needed (and using -0 as list index will cause problems)
        lst = lst[:1] + lst[-day:] + lst[1:-day]
    # pair off - zip the first half against the second half reversed
    half = num_teams // 2
    return list(zip(lst[:half], lst[half:][::-1]))
 
def make_schedule(num_teams):
    """
    Produce a double round-robin schedule
    """
    # number of teams must be even
    if num_teams % 2:
        num_teams += 1  # add a dummy team for padding

    # build first round-robin
    schedule = [make_day(num_teams, day) for day in range(num_teams - 1)]
    # generate second round-robin by swapping home,away teams
    swapped = [[(away, home) for home, away in day] for day in schedule]

    return schedule + swapped


def crear_fixture(equipos_dict, fixture_numeros):
    fixture =[]
    fixture_t=[]
    fixture_t2=[]

    #Haré un randomizado de los equipos, para que en el fixture no siempre salga el mismo orden de equipos:
    keys = list(equipos_dict.keys())

    random.shuffle(keys)

    equipos_dict2 = {}
    for i in range(1, len(equipos_dict) + 1):
        equipos_dict2[i] = equipos_dict[keys[i - 1]]

    for i in range(len(fixture_numeros)):
        for j in range(len(fixture_numeros[i])):
            for k in range(len(fixture_numeros[i][j])):
                fixture_t.append(equipos_dict2[fixture_numeros[i][j][k]])
            fixture_t2.append(fixture_t)
            fixture_t=[]
        fixture.append(fixture_t2)
        fixture_t2=[]
    return fixture


    
