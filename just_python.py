#%%
#Lists
number = [1, 2, 3]
print(number[-1])
#%%
number[0] = 5
print(number)

#%%
print(len(number))

#%%
number.append("peppy")
print(number)

#%%
smtg = [4, 5, 6]
print(number)

#%%
sugar = ["emtg, smtg"]
number.append(sugar)

#%%
print(number)

 #%%
number.insert(2, "potpie")
print(number)

#%%
number.remove("potpie")
print(number)

#%%
x = number.pop()
print(x)
print(number)

#%%
x = number.pop(1)
print(x)
print(number)

#%%
print(5 not in number)

#%%
for f in number:
    print(f)

#%%
x = number[:4]
print(x)

#%%
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[-1:-6:-2])


#%%
original = [10, 20, 30]
copy = original.copy()

print(original)
print(copy)

#%%
copy.append(40)
print(copy)

#%%
print(original)

#%%
a = [1, 2, 3]
b=a
b[0] = 100
print(a)
print(b)

#%%
x = 5, 6, 7, 8, 9
print(type(x))

#%%
fruits = ("apple", "banana", "mango")
single = (42,)
print(fruits)
print(single)
print(type(fruits))
print(type(single))

#%%
numbers = (10, 20, 30, 40, 50)
print(numbers[0])
print(numbers[-1])
print(numbers[2])
print(len(numbers))

#%%
print(numbers[1:4])
print(numbers[0:5:2])

#%%
print(numbers[::-1])
print(numbers[-1:-4:-2])

#%%
print(len(numbers))
print(30 in numbers)
print(100 not in numbers)
for num in numbers:
    print(num)

more_numbers = numbers + (60, 70)
print(more_numbers)

#%%
repeated = more_numbers * 2
print(repeated)

#%%
person = ("bob", 25)
name, age = person
print(name)
print(age)

#%%
nums = (10, 20, 30, 40, 50)
first, *rest = nums
print(first)
print(rest)

#%%
first, *middle, last = nums
print(first)
print(middle)
print(last)

#%%
numbers = (5, 10, 5, 20, 5, 30, 10)
print(numbers.count(5))
print(numbers.count(10))
print(numbers.index(20))
print(numbers.index(10))
print(numbers.index(100))

#%%
data = ([10, 20], "hello", 42)
data[2] = 100
data[1] = "bye"
data[0][1] = 99
print(data)

#%% 
a = "hello"
b= 'hello'
print(a == b)

#%%
a= "Mick"
b = "python is awesome"
c = """This is
a multiline
string"""
print(a)
print(b)
print(c)
list_of_strings = [a, b, c]
for stuff in list_of_strings:
    print(type(stuff))

#%%
word = "Programming"
print(word[0])
print(word[-1])
print(word[4])
print(word[-3])

#%%
print(word[:3])
print(word[3:7])
print(word[5:11])
print(word[:11:2])
print(word[::-1])

#%%
a = "cat"
b = "b" + a[1:]
print(b)

#%%
c = "cat"
d = c
d = "dog"
print(c)
print(d)

#%%
first = "Python"
second = "works"
print(first + second)
print("-" * 20)

#%%
text = "Python programming"
print("Python" in text)
print("Java" in text)
print("Java" not in text)

for t in text:
    print(t)

for s in text:
    if s == "o":
        print(s)

#%%
text = "pYTHON iS aWESOME"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text)

#%%
text = "     Python is awesome     "
print(text)
print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text)

#%%
text = "Python programming is fun. Python is powerful."
print(text.find("programming"))
print(text.index("Python"))
print(text.find("Java"))
print(text.count("Python"))
print(text.count("is"))

#%%
text = "Pep and Mol are in Vipraj"
print(text.replace("Vipraj", "The Majestic"))
print(text.startswith("Pep"))
print(text.endswith("Majestic"))
mtext = ("12345")
print(text.isdigit())
print(text[0].isalpha())
stext = "Python123"
print(stext.isalnum())
ptext = "Python 123"
print(ptext.isalnum())
print(text)

#%%
text = "Python is really really fun"
result = text.split()
print(result)
print(type(result))
data = "apple,banana,mango,dragonfruit"
data_result = data.split((","))
print(data_result)
print(text)
print(data)

#%%
words = ["Python", "is", "really", "fun"]
res = ", ".join(words)
print(res)
print(words)

#%%
fruits = ["apple", "banana", "mango"]
res = "|".join(fruits)
print(res)

#%%
name = "Alice"
age = 25
city = "Bangalore"
print(f"{name} is {age} years old and lives in {city}.")

#%%
a = 15
b = 7
print(f"The first result: {a + b} and the second result: {a * b}.")

#%%
price = 1234.5678
print(f"{price:.2f}")

#%%
x = 9.876

print(f"{x:.1f}")
print(x)

#%%
name = "Alice"
score = 0.92345
print(f"{name} scored {score:.2%}")

#%%
name = "Alice"
score = 92.5
print(f"{name:10} {score:.2f}")

#%%
text = "Python is fun"
print(len(text))
num = str(42)
print(type(num))

#%%
print(ord("B"))
print(chr(67))

#%% 
text = "Python"
print(len(text))
print(ord("a"))
print(chr(121))
print(type(str(2026)))

#%%
print(f"She said, \"Python is fun!\"\nAnd then she left.")

#%%
print(r"C:\Users\Alice\Documents\Python")

#%%
#Sets: Repeated values do not survive.
numbers = {1, 1, 2, 3, 4, 5}
print(numbers)
print(type(numbers))

#%%
fruits = {"apple", "banana", "mango", "apple", "orange", "banana"}
print(type(fruits))
print(fruits)
print(len(fruits))

#%%
numbers = [10, 20, 20, 30, 30, 30, 30, 40, 40]
unique_numbers = set(numbers)
print(unique_numbers)
print(len(unique_numbers))

#%%
empty = {}
print(type(empty))
print(len(empty))
print(empty)

#%%
numbers = {10, 20, 30}
x = numbers.add(40)
print(numbers)
print(len(numbers))

#%%
c = numbers.add(50)
print(numbers)
#Note: The add() method does not return any value, it modifies the set in place. Therefore, x and c will be None.

#%%
fruits.discard("strawberry")
print(fruits)
#remove() raises a KeyError if the element doesn't exist but discard() removes the element if it exists but doesn't give an error if it's absent. 

#%%
numers = {10, 20, 30, 40}
x = numers.pop()
print(x)
print(numers)

#%%
numers.clear()
print(numers)

#%%
#Membership & Iteration
fruits = {"apple", "banana", "mango", "orange"}
print("banana" in fruits)
print("grape" in fruits)
print("grape" not in fruits)

#%%
#Iterating over a set
fruits = {"banana", "apple", "mango"}
for x in fruits:
    print(x)

#%%
numbers = {10, 20, 30, 40, 50}
for c in numbers:
    print(c)
#Note: Sets don't guarantee the order in the o/p

#%%
print(len(numbers))
#len() behaves differently depending
#on the data structure
#for sets it returns the number of 
#unique elements
#for lists it returns the actual
#length. 
#len() itself doesnt remove the dupes
#set() does.

#%%
numbers = {10, 10, 20, 30, 30, 30, 40}
print(numbers)
print(len(numbers))

#%%
nums = [10, 20, 30, 40, 30, 40]
uniq_nums = set(nums)
print(nums)
print(uniq_nums)

#%%
fruits = ["apple", "banana", "apple", "mango", "banana", "orange"]
unique_fruits = set(fruits)
print(unique_fruits)
print(len(unique_fruits))

#%%
#Union
#Union takes everything from both
#sets but only keeps the 
#unique elements.
a={1, 2, 3}
b={3, 4, 5}
res = a|b
print(res)

#%%
#Intersection
#Returns only elements present
#In both sets
result = a&b
print(result)

# %%
#Difference: Whats in the
#first set but not in the 
#second set. 
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a-b)
#Note: the order matters, and its
#not actually subtracting values. 

#%%
#Symmetric Difference: elements
#that are in either set but
#not in both. 
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a^b)

#%%
#Method Versions of the ops
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

#%%
#Comparing Sets
#1. Subsets
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))
#Shorthand: a<=b

#%%
#2. Superset
print(b.issuperset(a))
#Shorthand: a>=b

# %%
#Disjoint sets: Ntg in common
a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))

#%%
#Adding elements from another collection into an existing set
nums = {1, 2, 3}
nums.update({20, 30, 40})
print(nums)

#%%
#Frozen Sets
numbers = frozenset({10, 20, 30})
print(numbers)
print(type(numbers))

# %%
#A normal set cannot itself be an element of another set.
#but you can have a set contain multiple frozen sets
#because frozen sets are immutable
#their hashing would remain unbroken

#%%
#Dictionaries
#A list lets you find something using a position. 
#A dictionary allows you to do that using a key. 

person = {
    "name": "Peppy",
    "age":  0.5,
    "home" : "Majestic"
}
print(person["age"])

# %%
#Adding a new key value pair. 
car = {
    'brand': "Honda",
    'model': "City",
    'year': 2014
}
car['colour'] = 'blue'
print(car)
#This allows to create a key that didn't exist
#and to update the value of one. 

# %%
#Removing dictionary items
year = car.pop('year') #removes a key and gives its value back
print(year)
print(car)

#%%
del car['brand']
print(car)
#Del simply removes it without giving the value back


# %%
item = car.popitem()#KV pair
print(item)
print(car)

# %%
car = {
    "brand": "Honda",
    "model": "City",
    "year": 2014
}

print("brand" in car)
print("Honda" in car)
print("year" in car)
print("colour" not in car)
#Note: membership checks for the key, not the value. 

#%%
student = {
    "name": "Mihika",
    "age": 21,
    "branch": "Mechatronics"
}

#this only prints the keys:
for item in student: #can also use .keys()
    print(item)

#this prints the values:
for x in student.values():
    print(x)

#this prints keys and values:
for k, v in student.items():
    print(k, v)

#%%
student.get("year")

#%%
#Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]

result = {x: x * 10 for x in numbers}

print(result)
# %%
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)

#%%
numbers = [2, 4, 6, 8, 10]
result = {x: x/2 for x in numbers}
print(result)

#%%
a = {"name": "Mihika", "age": 21}
b = {"age": 22, "branch": "Mechatronics"}

combined = {**a, **b}

print(combined)

#%%
numbers = [1, 2, 1, 3, 2, 1, 4, 3]
counts = {}
for x in numbers:
    if x in counts:
        counts[x] +=1
    else:
        counts[x] = 1

print(counts)