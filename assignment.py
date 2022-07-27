# This program adds two numbers

num1 = 1
num2 = 2

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum is:', sum)

# finding the Average of 2 numbers given by Valar Mam

A = 1
B = 2

# avg

avg = (A + B) / 2
print("average of A & B =", avg)

# finding the apple task given by Valar Mam

my_list = ["apple", "banana", "cherry"]
# if element present then return
# exist otherwise not exist
# Checking if apple exists in list
#print("for apple in test_list:")
if "apple" in my_list:
    print("apple Exists")
else:
    print("apple dose not exist")

#  change value of first item to "mango" in the given list by valar mam

my_list[0]="mango"
print("after changing value",my_list)

#how will you insert new element 'watermelon' to then given list

my_list.append("watermelon")
print("after adding new element",my_list)

# create a tuple with only one item and will tuple allow  duplicate values explain with examples

names=('valr','valr','karthi', 'balaji','valr')

print('names',names)

animals=('Valar',)
print('list of animals',animals)

# create dictionary and get value of first key?

useless = {1:'Amma',2:'Amma1', 'valar':'very useless'}
print("list of useless things",useless)
useless[1]
print('first element',useless[1])

#will dictionary allows duplicate values with same key ? explain with example?

useless = {1:'Amma',1:'Amma', 'valar':'very useless'}
print('check for duplicate',useless)

#Create set and delete the last element from set by valar mam.

a={1,2,3,4,5}
a.remove(5)
print("removing the last element",a)

#A = {1, 2, 3, 4, 5} and B = {4, 5, 6, 7, 8} are two set elements .how will you get the common elements from in both the sets?

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("intersection",a.intersection(b))





