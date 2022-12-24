# parking lot

from os import system
system ("cls")

p = ["Mercedes", None, "BMW", None, None, "Toyota", "BMW" ] # list of None type

#HW: calculate/print stats
print ("Statistic for parked car:")
n = 0
b = 0
t = 0
m = 0
for i in range (len(p)):
    if p[i] == None: 
        n += 1
    if p[i] == "BMW": 
        b += 1
    if p[i] == "Toyota": 
        t += 1
    if p[i] == "Mercedes": 
        m += 1    
print ( "None:", n)
print ("BMW:", b)
print ("Toyota:", t)
print ("Mercedes", m)



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


for i in range (len(p)):
    print (i, p[i])