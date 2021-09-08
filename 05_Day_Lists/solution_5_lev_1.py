# 1 Declare an empty list
empty_list = []
print(len(empty_list))

# 2 Declare a list with more than 5 items
list_1 = [ 'History', 'Math','Chemistry', 'Biology', 'Physics']

# 3 Find the length of your list
print(len(list_1))

# 4 Get the first item, the middle item and the last item of the list
print(list_1[0:5:2])

# 5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Betiana', 27, 1.60, 'Single', 'Merlo']

# 6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7 Print the list using print()
print(it_companies)

# 8 Print the number of companies in the list
print(len(it_companies))

# 9 Print the first, middle and last company
print(it_companies[0:7:3])

# 10 Print the list after modifying one of the companies
it_companies[5] = 'Twitter'
print(it_companies)

# 11 Add an IT company to it_companies
it_companies.append('Lenovo')
print(it_companies)

# 12 Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Samsung')
print(it_companies)

# 13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14 Join the it_companies with a string '#;  '
print('#; '.join(it_companies))

# 15 Check if a certain company exists in the it_companies list.
does_exist = 'Microsoft' in it_companies
print('Microsoft in it_companies?:', does_exist)  

# 16 Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17 Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

# 18 Slice out the first 3 companies from the list
print(it_companies[0:3])

# 19 Slice out the last 3 companies from the list
print(it_companies[-3:])

# 20 Slice out the middle IT company or companies from the list
middle = len(it_companies)//2
print(it_companies[0:middle])

# 21 Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# 22 Remove the middle IT company or companies from the list
del it_companies[middle]
print(it_companies)

# 23 Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# 24 Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25 Destroy the IT companies list
del it_companies

# 26 Join the following lists.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join_list = front_end +back_end
print(join_list)

# 27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = join_list
redux_index = full_stack.index('Redux') 
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print(full_stack)