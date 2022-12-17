from os import system
system ("cls")
# 1 create list
people = ["Marry", 20, "John", 21, "Peter", 22]
# 2 people count
n = []
for i in people:
    if (type(i) is str):
        n.append(i)
people_count = len(n)
print ("people count: ",people_count)

print()
# 4. create 2 variables
people_names = []
people_ages = []
# 5 divide name from age from list
for j in people:
    if (type(j) is str):
        people_names.append(j)
    else:
       people_ages.append(j)
print ("People names:", people_names)
print("People age:", people_ages)
        
print()
#6 input index

nr_idx = input("Enter index to find data:")
n_idx = int(nr_idx)
print (people_names[n_idx], people_ages[n_idx])

print()
#7 input name, find name place + then show age +
# if not found person does not exist

name_idx = input ("Enter name to find index:" )
name_x = people_names.index(name_idx)
print ("Person index:", name_x)
print("Person age",people_ages[name_x])


print()

# 8. Change age +
new_data = input("New person data:")
new_data = new_data.split()
new_pers_data = people_names.index(new_data[0])
people_ages [new_pers_data] = int (new_data[1])
print(people_ages)

print()
# 9. delete person data
delete_person = input ("Delete person:")
delete_x = people_names.index(delete_person)
people_names.pop (delete_x)
people_ages.pop (delete_x)
print("New list:")
print(people_names)
print (people_ages)

print()
#10. add new person data

new_person = input("Add new person:")
new_person = new_person.split()
people_names.append(new_person[0])
people_ages.append(new_person[1])
print("New list:")
print(people_names)
print (people_ages)

print()
# 11 insert in certain place new person ???

new_person = input("Add new person at specific place:")
new_1 = new_person.split()
people_names.insert (int (new_1 [2]), new_1[0])
people_ages.insert (int (new_1 [2]), new_1[1])
print (people_names)
print (people_ages)

print()
    


    
