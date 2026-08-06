# Exercise : Day 7


# Level 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add("Twitter")
print(it_companies)

it_companies.update(["Tesla","Snapchat","Reddit"])
print(it_companies)

it_companies.remove("IBM")
print(it_companies)

# remove : works on set and list but if the element is not present in the set or list then it will throw an error
# discard : works on set  but if the element is not present in the set then it will not throw an error

# Level 2

C=A.union(B)
print(C)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

D=B.union(A)
print(C)
print(D)

print(A.symmetric_difference(B))

del A
del B
del C
del D

# Level 3

ages=set(age)
if len(ages)>=len(age):
    print("Length of ages is greater than or equal to length of age")

else:
    print("Length of ages is less than length of age")

# string - contains text and numbers
# list - contains all type of data types and is mutable
# tuple - contains all type of data types and is immutable
# set - contains all type of data types but must be same datatype and is mutable but does not allow duplicates

# not came








