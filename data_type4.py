# String data type

# literal assignment
first = "Mayank"
last = "Agrahari"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

#constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

#concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + 's'
print(statement)

#multiple lines
multiline = '''
Hey, how are you?                             

I was just checking in.               
                                 All good?
'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

sentence = 'I\'m back at work!\tHey!\nWhere\'s this at\\located?'
print(sentence)

#string methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                          "
multiline = "                " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print('Coffee'.ljust(16,".") + "$1".rjust(4))
print('Bunmuska'.ljust(16,".") + "$3".rjust(4))
print('Tea'.ljust(16,".") + "$2".rjust(4))

#string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

#some methods return boolean data
print(first.startswith("M"))
print(last.endswith("i"))

#boolean data type (means true/false data type)
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

print("  ")

#float type (decimal type)
gpa = 3.289
y = float(1.14)
print(type(gpa))

#complex types
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#built-in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))

print(round(gpa, 2))

import math 

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

#error if you attempt to cast incorrect data
#zip_value = int("New York")
