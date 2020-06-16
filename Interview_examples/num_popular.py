#!/usr/bin/env python3
"""Python script to get the most repeated number from a list
if there are 2 with equal frecuent numbers it gets the biggest"""


def NumMasPopular(lista, lenght):
    dic = {}
    for i in range(0, lenght):
        dic.setdefault(lista[i], 0)
        dic[lista[i]] = dic[lista[i]] + 1
    sort_dic = sorted(dic, key=dic.get, reverse=True)
    first = sort_dic[0]
    second = sort_dic[1]
    if dic[first] == dic[second]:
        return first if first > second else second
    else:
        return sort_dic[0]

# Example

lista = [2, 2, 2, 2, 3, 3, 3, 3]
NumMasPopular(lista, len(lista))
