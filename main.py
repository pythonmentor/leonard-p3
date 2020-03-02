lab = []
with open('map.txt', 'r') as file:
    print(file)
    for line in file:
        l = list(line)
        l = ['m' if x == ' ' else x for x in l]
        l.remove('\n')
        lab.append(l)

lab[1][5] = 'start'
lab[13][5] = 'arrival'
print(lab[1])
print(lab[13])

# lab[1][0] = 'm'
# print(lab[1])
# print(lab)

# for char in lab:
#     if char == ' ':
#         lab[char] = 'm'
# print(lab)
