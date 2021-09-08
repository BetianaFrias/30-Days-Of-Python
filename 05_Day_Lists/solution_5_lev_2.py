ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1 Sort the list and find the min and max age
ages.sort()
print(ages)
print(min(ages))
print(max(ages))

# 2 Add the min age and the max age again to the list
minim = min(ages)
maxim = max(ages)
ages.append(minim)
ages.append(maxim)
print(ages)

# 3 Find the median age (one middle item or two middle items divided by two)
middle = len(ages) //2
print(ages[middle])

# 4 Find the average age (sum of all items divided by their number)
average = sum(ages) / len(ages)
print(average)

# 5 Find the range of the ages (max minus min)
range_ages = maxim - minim
print('Range:', {range_ages})

# 6 Compare the value of (min - average) and (max - average), use abs() method
value = abs(minim - average)
value_2 = abs(maxim - average)
print(f'min - average:{value} . Max - average:{value_2}')
