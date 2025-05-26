mystring = "hello world"

# length
print(len(mystring))

# count
print(mystring.count("l"))

# index
print(mystring.index("o"))

# lower
print(mystring.lower())

# upper
print(mystring.upper())

# split
mylist = mystring.split(" ")
print(mylist)

# join
mystringJoined = " ".join(mylist)
print(mystringJoined)

# slice
print(mystring[3:7])
print(mystring[3:])

# step
print(mystring[::2]) 

# reverse
print(mystring[::-1])

