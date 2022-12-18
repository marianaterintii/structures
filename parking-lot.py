# parking lot

from os import system
system ("cls")

p = ["Mercedes", None, "BMW", None, None, "Toyota", "BMW" ] # list of None type

#HW: calculate/print stats

from collections import Counter
ListCount = Counter(p)

print ("Statistic for parked car:")
for i in ListCount.items():
    print ( i[0],":", i[1])

print()


user_car_brand = input ("name your brand:?")
user_park_index = int (input ("What place:?"))
if p [user_park_index] == None:
    print ("ok, you can park there!!")
    p [ user_park_index] = user_car_brand
else:
    print ("This place is occupied!!")

# free/total
total = len(p)
free = 0
for i in range (len(p)):
    if p[i] == None:
        free += 1

print ( "Parking (free/total):", free, "/", total, "places")