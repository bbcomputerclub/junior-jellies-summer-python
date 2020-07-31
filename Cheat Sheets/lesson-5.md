# Lesson 5

- Libraries/Modules
- While loops
- For loops
---


## Libraries/Modules

Modules are code that someone else made, that we can import into our code and use.

### Importing random

```py
import random
```
To assign a pseudo-random number (from 0 - 64 inclusive) to a variable called number
```py
import random

number = random.randint(0, 64)

print(number)
```

To import a specific property from a module
```py
from random import randint
```

To assign a pseudo-random number (from 0 - 64 inclusive) to a variable called number

```py
from random import randint

number = randinit(0, 64)

print(number)
```
---
# While loops

```py
while True:
```

### Break

To stop a while loop from running, use ```break```
```py
while True:
  break
```

Looping and printing "Hello, World" until the variable number reaches five
```py
number = 0

while True:

  print("Hello, World")
  number += 1
  
  if number == 5:
    break
```

### Continue

If you want to skip the current loop and move on to the next loop 

```py
number = 0
while True:

  if number == 13:
    continue
    # 13 doesn't get printed as the while loop continues on to 14
  
  print(number)
  if number == 20:
    break
```
### Using Boolean Statements

You can replace "True" with a boolean statement

```py
number = 0

while number < 5:
  print("Hello World")
  number += 1
```

One last example:

```py
number = 0

while number != 10:
  print(number)
  number += 1
```
---
# For loops

Use for loops to iterate through an array or run a loop a specific amount of time

Using for loops to iterate through an array
```py
array = ["Elliot", "Bryant", "Allen", "Johnny"]

for name in array:
  print(name)
```

Using a for loop to loop 10 times
```py
for number in range(10):
  print(number)
```

You can use break/continue

```py
array = ["Johnny", "Elliot", "Allen", "Bryant"]

for name in array:
  if name == "Johnny":
    continue
    # "Johnny does not get printed"
  else if name == "Allen":
    break
    # the loop stops
  else:
    print(name)
```
