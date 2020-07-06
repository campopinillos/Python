#!/usr/bin/env python3
"""Fantasy Game Inventory Exercise"""


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(v, k)
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems=[]):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'arrow']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = addToInventory(stuff, dragonLoot)
displayInventory(inv)