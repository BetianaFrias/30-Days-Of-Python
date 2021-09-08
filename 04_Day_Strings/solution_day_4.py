# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string_1 = 'Thirty '
string_2 = 'Days '
string_3 = 'Of '
string_4 = 'Python'
concat_1 = string_1 + string_2 + string_3 + string_4
print(concat_1)

# 2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string_5 = 'Coding'
string_6 = 'For'
string_7 = 'All'
print(string_5 + ' ' + string_6 + ' ' +string_7)

# 3 Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# 4 Print the variable company using print().
print(company)

# 5 Print the length of the company string using len() method and print().
print(len(company))

# 6 Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7 Change all the characters to uppercase letters using upper() method.
print(company.lower())

# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9 Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))

# 11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# 12 Change Python for Everyone to Python for All using the replace method or other methods.
sentence_1 = 'Python For Everyone'
print(sentence_1.replace('Everyone', 'All'))

#  13 Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(', '))

# 15 What is the character at index 0 in the string Coding For All.
print(company[0])

# 16 What is the last index of the string Coding For All.
print(company[-1])

# 17 What character is at index 10 in "Coding For All" string.
print(company[10])

# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
words = sentence_1.split(' ') 
character = ''

for word in words:
   character += word[0]

print(character)

# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
words_2 = company.split(' ') 
char = ''

for word in words_2:
   char += word[0]

print(char)

# 20 Use index to determine the position of the first occurrence of C in Coding For All.
find_c = 'C'
print(company.index(find_c))
 
# 21 Use index to determine the position of the first occurrence of F in Coding For All.
find_f = 'F'
print(company.index(find_f))

# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
phrase = 'Coding For All People'
print(phrase.rfind('l'))

# 23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence_2 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence_2.find('because'))
print(sentence_2.index('because'))

# 24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence_2.rindex('because'))

# 25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
words_3 = sentence_2.split()
print(words_3[6:9])

# 26 Does ''Coding For All' start with a substring Coding?
print(company.startswith('Cod'))

# 27 Does 'Coding For All' end with a substring coding?
print(company.endswith('ing'))

# 28 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
sentence_3 = '   Coding For All      '
print(sentence_3.strip(' '))

# 29 Which one of the following variables return True when we use the method isidentifier(): 30DaysOfPython | thirty_days_of_python
variable_1 = '30DaysOfPython'
variable_2 = 'thirty_days_of_python'
print(variable_1.isidentifier())
print(variable_2.isidentifier())

# 30 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
list_1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(list_1))

# 31 Use the new line escape sequence to separate the following sentences. I am enjoying this challenge. | I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')

# 32 Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
line_1 = 'Name\tAge\tCountry\tCity\t'
print(line_1.expandtabs(12))

line_2 = 'Asabeneh\t250\tFinland\tHelsinki'
print(line_2.expandtabs(12))

# 33 Use the string formatting method to display the following:
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square')

# 34 Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
nbr_1 = 8
nbr_2 = 6
total = nbr_1 +nbr_2
diff = nbr_1 - nbr_2
prod = nbr_1 * nbr_2
div = round(nbr_1 / nbr_2,2)
rem = nbr_1 % nbr_2
floor_div = nbr_1 // nbr_2
exp = nbr_1 ** nbr_2
print(f'{nbr_1} + {nbr_2} = {total}')
print(f'{nbr_1} - {nbr_2} = {diff}')
print(f'{nbr_1} * {nbr_2} = {prod}')
print(f'{nbr_1} / {nbr_2} = {div}')
print(f'{nbr_1} % {nbr_2} = {rem}')
print(f'{nbr_1} // {nbr_2} = {floor_div}')
print(f'{nbr_1} ** {nbr_2} = {exp}')
