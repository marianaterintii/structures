
from os import system
system ("cls")

people = ["Johny", "Marry", "Francis"] # top 3 developers in a company

print ("BEFORE", people)
# traingle solution
temp     = people[0] # "Johny"
people[0] = people[1] # Marry -> Johny
people[1] = temp      # Johny -> Marry
print ("AFTER", people)

print()
#HW: add code -> user -> place A, place B
#HW* check boundaries - does not exist ?????

placeA = int (input("Place to change?: "))
placeB = int (input("To which place?: "))

temp_1 = people  [placeA]
people [placeA] = people [placeB]
people [placeB] = temp_1
print ("AFTER", people)




     
print()