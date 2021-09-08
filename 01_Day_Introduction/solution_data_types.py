'''Level 3
Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
'''

print('\nExercise 1')
print('Different Python data types')
print('\n')
print(324, type(8.3))
print(98.23, type(98.23))
print(9 + 2j, type(9 + 2j))
print('wonderwall', type('wonderwall'))
print(False, type(False))
print(['star', True, 2], type(['star', True, 2]))
print(('bubble', 4.5, 88), type(('bubble', 4.5, 88)))
print({'yellow', 'submarine'}, type({'yellow', 'submarine'}))
print({'name': 'Louis'}, type({'name': 'Louis'}))



'''Find an Euclidian distance between (2, 3) and (10, 8)'''

print('\nExercise 2')

first_point_x = 2
first_point_y = 3
second_point_x = 10
second_point_y = 8

distance = ((second_point_x - first_point_x)**2 + (second_point_y - first_point_y)**2)** 0.5

print(f'The Euclidean distance between (2,3) and (10,8) is {distance}')