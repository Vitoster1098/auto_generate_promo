import random
from itertools import groupby
from userdata import amount_keys


def init():
    Altha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    list = []
    x = 0
    print("Amount of keys")
    # y = int(input())
    y = int(amount_keys)

    while x != y:
        x += 1
        Rand = f"{random.choices(Altha, k=4)}-{random.choices(Altha, k=4)}-{random.choices(Altha, k=4)}-{random.choices(Altha, k=4)}"
        st = Rand.replace("'", "")
        nd = st.replace(",", "")
        rd = nd.replace("[", "")
        last = rd.replace("]", "")
        lastplus = last.replace(" ", "")
        list.append(lastplus)

    newlist = [el for el, _ in groupby(list)]

    MyFile = open('keys.txt', 'w')

    for element in newlist:
        MyFile.write(element)
        MyFile.write('\n')

    MyFile.close()
    return newlist
