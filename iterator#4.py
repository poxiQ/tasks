import itertools


def generate(count):
    first = int(("10" * count), 2)
    mass = [i for i in "10" * count]
    perm_set = itertools.permutations(mass)
    mass.clear()
    for i in set(perm_set):
        if int(''.join(i), 2) % 2 == 0 and int(''.join(i), 2) >= first:
            mass.append(int(''.join(i)))
    mass.sort()
    count = ""
    arr = []
    for i in mass:
        for j in str(i):
            count += "(" if j == "1" else ")"
        arr.append(count)
        count = ""
    return arr


print(generate(3))



