# FACT: list of friends

#empty list
friends = []

while  len (friends) < 5:
    name = input("Add friend name: ")
    if name == "":
        break
    if name in friends == friends:
           print ("name used")
    else:
        friends.append ( name )


print ("You have", len (friends), "friends")
for i in range ( len(friends) ):
    print ( " ", i, ">>", friends [i])
