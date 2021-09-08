# 1 Declare your age as integer variable
my_age = 27
print('My age:', my_age, '\n')

# 2 Declare your height as a float variable
my_height = 1.60
print('My height:', my_height, 'm\n')

# 3 Declare a variable that store a complex number
complex_num = 4j - 5
print('Complex:', complex_num, '\n')

# 4 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base= float(input('Enter base: '))
height = float(input('Enter height: '))
area_triangle = round(base * height * 0.5, 2)
print(f'The area of the triangle is {area_triangle}')
print('\n')

# 5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input('Enter side a: '))
side_b = float(input('Enter side b: '))
side_c = float(input('Enter side c: '))
perim_triangle = round(side_a + side_b + side_c, 2)
print('The perimeter of the triangle is:', perim_triangle) 
print('\n')

# 6 Get length and width of a rectangle using prompt. Calculatel its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
lenght_rect = float(input('Enter lenght of the rectangle: '))
width_rect = float(input('Enter width of the rectangle: '))
perim_rect = round(2 * lenght_rect + 2 * width_rect, 2)
area_rect = round(lenght_rect * width_rect, 2)
print('The perimeter of the rectangle is:', perim_rect)
print('The area of the rectangle is:', area_rect)
print('\n')

# 7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
import math
radius_circle = float(input('Enter radius of the circle: '))
area_circle = round(math.pi * (radius_circle)**2, 2)
perim_circle = round(2 * math.pi * radius_circle, 2)
print('The area of the circle is:', area_circle)
print('The perimeter of the circle is:', perim_circle)
print('\n')

# 8 Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope_8 = 2
x_inter = 2 / 2
y_inter = -2
print(f'y = 2x - 2\nSlope = {slope_8}\nx-intercept = {x_inter}\ny-intercept = {y_inter}\n')

# 9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
(x1, y1) = (2,2)
(x2, y2) = (6,10)
slope_9 = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)* 0.5
print('The Euclidean distance between (2,2) and (6,10) is:', distance)
print('The slope is:', slope_9)
print('\n')

# 10 Compare the slopes in tasks 8 and 9
print('Is slope(task8) = slope(task9)?', slope_8 == slope_9) 
print('\n')

#11 Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at what x value y is going to be 0.
value_x1 = 2
value_x2 = 3
value_x3 = 4
y_1 = (value_x1)**2 + 6 *(value_x1) + 9 
y_2 = (value_x2)**2 + 6 *(value_x2) + 9 
y_3 = (value_x3)**2 + 6 *(value_x3) + 9 
a = 2
b = 5
c = -1
root_1 = (- b + (4 * a * c)** 0.5) / (2 * a)
root_2 = (- b - (4 * a * c)** 0.5) / (2 * a)

# 12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
lenght_py = len('python')
lenght_dra = len('dragon')
print(f'Lenght of "python" is not the same of "dragon":', lenght_py != lenght_dra)
print('\n')

# 13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('"on" is in "python"', 'on' in 'python')
print('"on" is in "dragon"', 'on' in 'dragon')
print('\n')

# 14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
word = 'jargon'
phrase = 'I hope this course is not full of jargon'
print(f'"{word}" is in "{phrase}": ', word in phrase)
print('\n')

# 15 There is no 'on' in both dragon and python
print('There is no "on" in both "dragon" and "python":', not ('on' in 'python' and 'on' in 'dragon'))
print('\n')

# 16 Find the length of the text python and convert the value to float and convert it to string
convert_word = str(float(len('python')))
print('Convert the lenght of the text python to string',type(convert_word))
print('\n')

# 17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
get_number = int(input('Enter a number: '))
if get_number % 2 == 0:
    print('It is an even number')
else:
    print('It is an odd number')
print('\n')

# 18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print('Floor division of 7 by 3 is equal to the int converted value of 2.7:', 7 // 3 == int(2.7))
print('\n')

# 19 Check if type of '10' is equal to type of 10
print('type of "10" is equal to type of 10:', type('10')== type(10))
print('\n')

# 20 Check if int('9.8') is equal to 10
#print('int("9.8") is equal to 10:', int_convert == 10) no puedo convertir el str 9.8 a int 

# 21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input('Enter hours: '))
rate = int(input('Enter rate per hour: '))
weekly_earning = hours * rate
print('Your weekly earning is:', weekly_earning)
print('\n')

# 22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
number_of_years = int(input('Enter number of years you have lived:'))
days_year = 365
hours_day = 24
seconds_hour = 3600
seconds_lived = number_of_years * days_year * hours_day * seconds_hour
print(f'You have lived for {seconds_lived} seconds')
print('\n')

# 23 Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
for i in range(1,6):
    print(i, i**0, i**1, i**2, i**3)