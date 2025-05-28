x=(10,20,30,40)
print(type(x))
print(x[3])

# list function
x=list(x)
print(type(x))
x.append(100)

# convert back to tuple
x=tuple(x)
print(x)

# days
days=('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
print(days)
#1. Find wednesday using an index
print(days[2])
#2. Using a function a find the length of the tuple.
print(len(days))
#3. Replace Thursday with Thur
days=list(days)
days[3]='thur'
days=tuple(days)
print(days)


