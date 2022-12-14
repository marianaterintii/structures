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
       (type(j) is int)
       people_ages.append(j)
print ("people names:", people_names)
print("people age:", people_ages)
        
print()
#6 input index
nr_idx = input("enter index:")

#show name/age 
# cum afisez numele si virsta de pe indice?

#7 input name, find name place + then show age -
# if not found person does not exist
name = [] 
name_idx = input ("Enter name:" )
name_x = people_names.index(name_idx)
print (name_x)

#cum extrag virsta utilizind valoarea

# 8. Change age ???
new_data = input("New data:")

# 9. delete person data
delete_person = input ("Delete person:")
delete_x = people_names.index(delete_person)
people_names.pop (delete_x)
people_ages.pop (delete_x)
print("New list:")
print(people_names)
print (people_ages)

#10. add new person data

new_person = input("Add new person:")
new_person = new_person.split()
people_names.append(new_person[0])
people_ages.append(new_person[1])
print("New list:")
print(people_names)
print (people_ages)

# 11 insert in certain place new person ???

new_person = input("Add new person idx:")

    


    
