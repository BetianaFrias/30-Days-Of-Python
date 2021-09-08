'''Exercises: Level 1
Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
Write a python comment saying 'Day 2: 30 Days of python programming'
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line'''

# Day 2: 30 Days of python programming
print('Level 1')
first_name = 'Ivan'
last_name = 'Bennet'
country = 'Argentina'
city = 'Merlo'
age = 28
year = 1987
is_married = False
is_true = True
is_light_on = False

print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Year:', year)
print('Is married:', is_married)
print('Is true:', is_true)
print('Is light on:', is_light_on)

first_name, last_name, country, city, age, year, is_married, is_true, is_light_on  = 'Lara', 'Martinez', 'Colombia', 'Caracas', 32, 2019, True, False, True
print('\nMultiple variable on one line:', first_name, last_name, country, age, year, is_married, is_true, is_light_on)


'''Exercises: Level 2
1. Check the data type of all your variables using type() built-in function
2. Using the len() built-in function, find the length of your first name
3. Compare the length of your first name and your last name
4. Declare 5 as num_one and 4 as num_two
 a.Add num_one and num_two and assign the value to a variable total
 b.Subtract num_two from num_one and assign the value to a variable diff
 c.Multiply num_two and num_one and assign the value to a variable product
 d.Divide num_one by num_two and assign the value to a variable division
 e.Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
 f.Calculate num_one to the power of num_two and assign the value to a variable exp
 g.Find floor division of num_one by num_two and assign the value to a variable floor_division
5.The radius of a circle is 30 meters.
 a.Calculate the area of a circle and assign the value to a variable name of area_of_circle
 b.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
 c.Take radius as user input and calculate the area.
6.Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names'''


#1
print('\nLevel 2')
print('Type first_name:', type(first_name))
print('Type last_name:', type(last_name))
print('Type country:', type(country))
print('Type city:', type(city))
print('Type age:', type(age))
print('Type year:', type(year))
print('Type is_married:', type(is_married))
print('Type is_true:', type(is_true))
print('Type is_light_on:', type(is_light_on))
print('\n')

#2
lenght_1 = len(first_name)
print(f'The lenght of first_name is {lenght_1}')

#3
lenght_2 = len(last_name)
print('Do first_name and last_name have the same lenght?:', lenght_1== lenght_2)
print('\n')

#4
num_one = 5
num_two = 4
print(f'The first number is {num_one}, the second number is {num_two}')
#4a
total = num_one + num_two
print(f'The sum is {total}')
#4b
diff = num_one - num_two
print(f'The difference is {diff}')
#4c
product = num_one * num_two
print(f'The product is {product}')
#4d
division = num_one / num_two
print(f'The result of the division is {division}')
#4e
remainder = num_one % num_two
print(f'The remainder of the division is {remainder}')
#4f
exp = num_one ** num_two
print(f'The power is {exp}')
#4g
floor_division = num_one // num_two
print(f'The result of the floor division is {floor_division}')
print('\n')

#5
radius = 30
import math
area_of_circle = round(math.pi * (radius ** 2),2)
circum_of_circle = round(2 * math.pi * radius, 2)
print(f'The radius is {radius}\nThe area of the circle is {area_of_circle}\nThe circumference of the circle is {circum_of_circle}\n')

radius_input = float(input('Introduce the radius of the circle: '))
import math
area_of_circle = round(math.pi * (radius_input ** 2),2)
circum_of_circle = round(2 * math.pi * radius_input, 2)
print(f'The radius is {radius_input}\nThe area of the circle is {area_of_circle}\nThe circumference of the circle is {circum_of_circle}\n')

#6
get_first_name = input('Introduce your first name: ')
get_last_name = input('Introduce your last name: ') 
get_country = input('Introduce your country: ')
get_age = input('Introduce your age: ')
print('\n')
print(f'First name: {get_first_name}\nLast name: {get_last_name}\nCountry: {get_country}\nAge: {get_age}')