# 1 Create an empty tuple
empty_t = ()
print(empty_t)

# 2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Araceli', 'Karen','Mayra','Bianca','Luz')
brothers = ('Franco', 'Agustin', 'Alexis')

# 3 Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

# 4 How many siblings do you have?
print(f'I have {len(siblings)} siblings')

# 5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
make_list = list(siblings)
make_list.append('Francisco')
make_list.append('Lucia')
family_members = tuple(make_list)
print(family_members)