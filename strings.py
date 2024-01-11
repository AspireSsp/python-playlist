# (: strings are immutable in Python :)
name = "sanjay"
ssp = 'sanjaufnkklnk'

print(name)
print(ssp)
# this is the way to declare the string;
var = "sajay is a good \"programmmer\", and the best coder"
var = 'sajay is a good "programmmer", and the best coder'
var = """sajay is a good \"programmmer\", 
and the best coder
i am also a fullstack developer"""
print(var)


# here we learn how to slice the string;
let = "my name is sanjay!!!"
print(let[3:7])
print(let[-4: -2])
print(let[len(let)-4: len(let)-2]) #above line work like this


# how to find the length of the string
print(len(let))

print(let.upper())
print(let.lower())
print(let.rstrip("!"))
print(let.replace("sanjay", "Aspire"))
print(let.capitalize())
print(let.count('a'))

# there are lots of many other string methods
# find(), index(),isalnum(), isalpha(), isdigit(), islower().............