# try:
# 	[1,2,3][4]
import math
import itertools


class test():
    id = 0

    def __init__(self, id):
        self.id = id
        id = 2


t = test(1)
t.id


[i for i in ifilter(lambda x: x % 5, islice(count(5), 10))]



df = {0: 'A',
 1: 'B',
 2: 'C',
 3: 'D',
 4: 'E',
 5: 'F',
 6: 'G',
 7: 'H',
 8: 'I',
 9: 'J',
 10: 'K',
 11: 'L',
 12: 'M',
 13: 'N',
 14: 'O',
 15: 'P',
 16: 'Q',
 17: 'R',
 18: 'S',
 19: 'T',
 20: 'U',
 21: 'V',
 22: 'W',
 23: 'X',
 24: 'Y',
 25: 'Z'}

{alphabet: number for number, alphabet in df.items()}
df

import pandas as pd
df = pd.DataFrame(['Braud, Mr. Owen Harris',
    'Cumings, Mrs. John Bradley',
    'Heikkeinen, Miss. Laina',
    'Futrelle, Mrs. Jacques Heath',
    'Allen, Mr. William Henry',
    'Moran, Mr. James'])

df['Title'] = df[0].apply(lambda a: a[a.find(',')+2: a.find('.')])

def isEven(anyInteger):
    return anyInteger % 2 == 0

myList = [0, 5, 10, 15, 20, 25, 30]
isEvenList = list(map(isEven, myList))
print(isEvenList)

isEvenList = []
for i in myList:
    isEvenList.append(isEven(i))

print(isEvenList)

even = list(filter(isEven, myList))

reduce()