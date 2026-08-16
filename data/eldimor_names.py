import random

_prefixes = ('Im', 'Hi', 'O', 'Pi', 'Fo', 'Sa', 'Mi', 'Ta', 'Dr', 'Dw', 'Ra', 'Sp', 'Jo', 'J', 'Gi', 'Ri', 'Do', 'Uk', 'Gr', 'Ge', 'U', 'Jo', 'Br', 'B', 'Da', 'Na', 'No', 'Ek', 'Ri', 'Ra', 'Lo')
_suffixes = ('ua', 'er', 'i', 'rl', 'ah', 'ke', 'ha', 'ip', 'ht', 'an', 'ur', 'il', 'ra', 't', 'la', 'ck', 'te', 'do', 'he', 'ge', 'et', 'a', 'ph', 'eh', 'd', 'ky', 'el')
_middles = ('k', 'l', 'r', 's', 'ig', 'd', 'a', 'er', 'an', 'tt', 'b', 'se', 'i', 'sh', 'bb', 'o', 'rr')

middle_chance = 0.75
middle_chance_x2 = 0.5
middle_chance_x3 = 0.25

def make_name():
    if random.uniform(0,1) < middle_chance:
        name = random.choice(_prefixes) + random.choice(_middles) + random.choice(_suffixes)
    elif random.uniform(0,1) < middle_chance_x2:
        name = random.choice(_prefixes) + random.choice(_middles) + random.choice(_middles) + random.choice(_suffixes)
    elif random.uniform(0,1) < middle_chance_x3:
        name = random.choice(_prefixes) + random.choice(_middles) + random.choice(_middles) + random.choice(_middles) + random.choice(_suffixes)
    else:
        name = random.choice(_prefixes) + random.choice(_suffixes)
    return name

if __name__ == '__main__':
    repeats = 0
    names = [make_name() for i in range(0,100)]
    for i, n in enumerate(names):
        if n in names[:i]:
            repeats != 1
        print(n)
    print(str(repeats) + ' repeats')