
numbers = [int(x) for x in input().split()] # N y K
form_names = [int(x) for x in input().split()] # Forms

inventory = {}
count = 0 #1
count1 = 0 
for p, v in enumerate(form_names):
    if v in inventory:
        count += 1
        if p - inventory.get(v, 0) <= numbers[1]:
            count1 += 1
    inventory[v] = p
    print(inventory)

print(count, count1)
