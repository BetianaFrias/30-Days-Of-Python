A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


# 1 Join A and B
join_set = A.union(B)
print(join_set)

# 2 Find A intersection B
inter_set = A.intersection(B)
print(inter_set)

# 3 Is A subset of B
print('Is A subset of B:', A.issubset(B))

# 4 Are A and B disjoint sets
print('Are A and B disjoint sets:', A.isdisjoint(B))

# 5 Join A with B and B with A
A.update(B)
print(A)

B.update(A)
print(B)

# 6 What is the symmetric difference between A and B
A.symmetric_difference(B)
print(B)

# 7 Delete the sets completely
del A
del B
