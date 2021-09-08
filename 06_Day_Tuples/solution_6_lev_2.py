#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'kiwi', 'strawberry')
vegetables = ('onion', 'potatoes', 'carrot','garlic')
animal_prod = ('butter','egg','milk', 'cheese')
food_stuff_tp = fruits + vegetables + animal_prod
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = len(food_stuff_tp)//2
print(middle)
print(food_stuff_tp[middle-1])

# Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[0:3]
print(first_three)

last_three = food_stuff_lt[-3:]
print(last_three)

# Delete the food_staff_tp tuple completely
del food_stuff_tp


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
print(f'Is Stonia a nordic country?:', 'Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print(f'Is Iceland a nordic country?:', 'Iceland' in nordic_countries)