## APP -> waiters
#one waiter -> 3 tables
from os import system
system ("cls")

food_name = [ "Pizza", "Salad", "Soup"]
food_price = [ 100.00,   50.00,  25.00]


status  = [ "free", "free", "free"]
client =  [ "    ", "    ", "    "]
order =   [ "    ", "    ", "    "]
bill =    [    0.0,    0.0,   0.0 ]
tip  =    [    0.0,    0.0,   0.0 ]

# 1. client " John" -> 3rd table

client[2] = "John"
status[2] = "not-free"

client[0] = "Marry"
status[0] = "not-free"

# 2. John orders a soup

client_name = "John"

food_order_name = input ("What would you like to order?:")

if food_order_name in food_name:
    print ("Great choose! will be ready in 15 min!")
else:
    food_order_name not in food_name
    print ("Sorry we don't have that! you can choose only from the menu")

print ()

client_idx = client.index(client_name)
order[client_idx] = food_order_name

food_idx = food_name.index (food_order_name)
bill[client_idx] = food_price[food_idx]
tip [client_idx] = bill[client_idx] /10

for ti in range (len(status)):
        print (f"table{ti+1} ({status[ti]}):")
        if status[ti] != "free":
            print(f"\t {client [ti]}")
        if bill [ti] == False:
            print (" ")
        else:
                print (f"\t { order[ti]} -> {bill [ti]} % {tip [ti]}")

print ()

        
