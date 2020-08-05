# Lesson 6

- Lists
- Loops
# List

- A list is a collection of variables that we can access. Inside of a list you can have any data type, including strings, integers, booleans, etc.

## Creating a list

To create a list:

```py
sports = ["baseball", "basketball", "football", "soccer"]
```

## List Index

To get a specific value from a list:

```py
foods = ["apple", "orange", "banana"]

print(foods[0]) # apple
print(foods[1]) # orange
print(foods[2]) # banana
```

## Length of the list

To get the length of the list:

```py
subjects = ["English", "Math", "Science", "History"]

print(len(subjects)) # 4
```
## Printing a list

There are two ways you can print a list

One way is to print the list as a whole (Not recommended)

```py
foods = ["apple", "banana", "cantaloupe"]
print(foods) 

# ['apple', 'banana', 'cantaloupe']
```

This is not the preffered way to print lists

The other way is by using a for loop to print each item in the list

```py
foods = ["apple", "banana", "cantaloupe"]

for food in foods:
  print(food)

# apple
# banana
# cantaloupe
```

As you can see, the first block of code prints the entire list in one line including the brackets and the quotation marks.
The second block of code prints each value of the list on each line

You can now see why many people prefer using the for loop to print out an list

To print all of the values in one line with a for loop:

```py
foods = ["apple", "banana", "cantaloupe"]

for food in foods:
  print(food, end=" ")

# apple banana cantaloupe
```
## Append

To add an item to the list:

```py
companies = ["Apple", "Google", "Amazon", "Facebook"]
companies.append("Netflix")

for company in companies:
  print(company, end=" ")

# Apple Google Amazon Facebook Netflix
```

## Remove

To remove an item from the list using the name of the value:

```py
companies = ["Apple", "Google", "Amazon", "Facebook"]
companies.remove("Google")

for company in companies:
  print(company, end=" ")

# Apple Amazon Facebook
```

## Pop

To remove the list item from the list:

```py
companies = ["Apple", "Google", "Amazon", "Facebook"]
companies.pop()

for company in companies:
  print(company, end=" ")

# Apple Google Amazon
```

---
# For loop

For loops are helpful for going through each item in the list.

For example:
```py
foods = ["apple", "banana", "cantaloupe"]

for food in foods:
  print(food, end=" ")

# apple banana cantaloupe
```

However, you don't need to have an array if you want to use loops

If you want to repeat a code a specified number of times:

```py
for number in range(10):
  print(number, end=" ")

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```