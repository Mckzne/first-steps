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