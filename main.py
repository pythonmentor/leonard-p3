lab = []
with open('map.txt', 'r') as file:
    print(file)
    for line in file:
        l = list(line)
        l.remove('\n')
        lab.append(l)

lab[1][0] = 'm'
print(lab[1])
print(lab)
