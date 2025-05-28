# 1. numbers = (10, 20, 30, 40, 50)Add 60 to the end,Replace 30 with 35.
numbers = (10, 20, 30, 40, 50)
numbers=list(numbers)
numbers.append(60)
numbers[2]=35
print(numbers)
# numbers=tuple(numbers)
# 2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order.
values = (15, 5, 30, 25, 10)
values=list(values)
print(values)
# 3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
# Count occurrences of "banana",Remove all occurrences of "banana".
fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
fruits=list(fruits)
fruits.count('banana')
print(fruits)
# 4. names = ("Alice", "Bob", "Charlie", "David") Reverse the order of elements using sort method.
names = ("Alice", "Bob", "Charlie", "David")
print(type('names'))
names=list('names')
names.sort(reverse=all)
names=str(names)
print(names)
# 5. colors = ("red", "blue", "green")add "yellow" at index 1,Extend with ["purple", "orange"]
colors = ("red", "blue", "green")
colors=list('colors')
colors.insert('yellow'[1])
colors.extend('purple' 'orange')
colors=str(colors)
print(colors)


