age = [22, 19, 24, 25, 26, 24, 25, 24]


# 1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_set = set(age)
print('Lenght list:', len(age))
print('Lenght set:', len(ages_set))

print('Is len(list) == len(set): ', len(age)==len(ages_set))
print('Is len(list) < len(set): ', len(age)>len(ages_set))
print('Is len(list) < len(set): ', len(age)<len(ages_set))

# 2 Explain the difference between the following data types: string, list, tuple and set
# La lista es mutable, puede ser modificada (agregar items, remover, etc). Una tupla no puede ser modificada, es inmutable. En ambas pueden repetirse elementos, en contraposicion a los sets , los cuales no tienen elementos duplicados.

# 3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
unique_words = set(sentence.split(' '))
print(unique_words)
