import itertools

letters = ('S','E','N','D','M','O','R','Y')

for perm in itertools.permutations('0123456789', 8):
    d = dict(zip(letters, perm))
    if d['S']=='0' or d['M']=='0': 
        continue

    SEND = int(d['S']+d['E']+d['N']+d['D'])
    MORE = int(d['M']+d['O']+d['R']+d['E'])
    MONEY = int(d['M']+d['O']+d['N']+d['E']+d['Y'])

    if SEND + MORE == MONEY:
        print("Solution:")
        print(d)
        break
