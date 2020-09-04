# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
for i in range(len(humans)):
  if humans[i].name.startswith('D'):
    a.append(humans[i].name)
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
for i in range(len(humans)):
  if humans[i].name.endswith('e'):
    b.append(humans[i].name)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []  # Only way I was able to get it to work
for i in range(len(humans)):
  if humans[i].name.startswith('C'):
    c.append(humans[i].name)
  if humans[i].name.startswith('D'):
    c.append(humans[i].name)
  if humans[i].name.startswith('E'):
    c.append(humans[i].name)
  if humans[i].name.startswith('F'):
    c.append(humans[i].name)
  if humans[i].name.startswith('G'):
    c.append(humans[i].name)
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
for i in range(len(humans)):
  d.append(humans[i].age + 10)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
for i in range(len(humans)):
  e.append(humans[i].name + '-' + str(humans[i].age))
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
for i in range(len(humans)):
  if humans[i].age in range(27,33):
    ag = humans[i].name , humans[i].age
    f.append(ag)
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
g = humans.copy()
for i in range(len(humans)):
  g[i].name = humans[i].name.upper()
  g[i].age = humans[i].age+5
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
for i in range(len(humans)):
  h.append(math.sqrt(humans[i].age))
print(h)
