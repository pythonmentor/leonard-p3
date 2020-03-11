LAB = []


def lab_surface():
    """ Define lab structure """
    with open('map.txt', 'r') as file:
        for line in file:
            a_list = list(line)
            a_list.remove('\n')
            LAB.append(a_list)
            print(line.strip())


lab_surface()


class MacGyver:
    """ class that define Mac Gyver character """
