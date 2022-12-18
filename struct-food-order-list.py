# order info -> lists

from os import system
system ("cls")

order_food_names = [ "Pizza", "Salad", "Soup"] # str
order_food_price = [  75.00,   45.00,   15.00] # float
order_food_quantity = [   2,       1,       2] # int

for i in range (len (order_food_names)):
    print (i+1, order_food_names[i], order_food_price[i], order_food_quantity[i])
print()

# HW - calculate total
order_food_names[0] = order_food_price [0]*order_food_quantity[0]
order_food_names [1] = order_food_price[1]*order_food_quantity[1]
order_food_names[2] = order_food_price [2] *order_food_quantity[2]
total_price = order_food_names [0] + order_food_names [1] + order_food_names [2]
print ("Total order price:",total_price)
print()

