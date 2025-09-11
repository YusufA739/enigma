list1 = ['a','b','c','d','e','f','g','h','i','j']
r1 = list1
temp = list1
r2 = []

for carrier in range(int(len(list1)/2)):
    r2.append(list1[carrier])
    temp.remove(list1[carrier])

