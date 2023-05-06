


#---------------------------------------
#------- Type converseion---------
#---------------------------------------

# str()

a = 10
print(type(a)) # <class 'int'>
print(type(str(a))) # <class 'str'>

print("-" * 50) # --------------------------------------------------


 # tuple()

s = "Salar" # String
d = [1,2,3,4,5] # List
f = {"A" , "B" , "C"} # Set
e = {"A" : 1 , "B" : 2 } # Dictionary

print(tuple(s)) # ('S', 'a', 'l', 'a', 'r')
print(tuple(d)) # (1, 2, 3, 4, 5)
print(tuple(f)) # ('B', 'A', 'C') #  unordered
print(tuple(e)) # ('A', 'B')

print("-" * 50) # --------------------------------------------------

# List()


s = "Salar" # String
d = (1,2,3,4,5) # Tuple
f = {"A" , "B" , "C"} # Set
e = {"A" : 1 , "B" : 2 } # Dictionary

print(list(s)) # ["s" , "a" , "l" , "a" , "r"]
print(list(d)) # [1, 2, 3, 4, 5]
print(list(f)) # ['A', 'C', 'B']
print(list(e)) # ['A', 'B']

print("-" * 50) # --------------------------------------------------

# Set()

s = "Salar" # String
d = (1,2,3,4,5) # Tuple
f = ["A" , "B" , "C" ] # list
e = {"A" : 1 , "B" : 2 } # Dictionary


print(set(s)) # {"s" , "r" , "a" , "a" , "l"}
print(set(d)) # {1, 2, 3, 4, 5}
print(set(f)) # {'B', 'C', 'A'}
print(set(e)) # {'B', 'A'}


print("-" * 50) # --------------------------------------------------

# dictionary()

s = "Salar" # String
d = (("A" , 1) , ("B" , 2) , ("C" ,3)) # Tuple
f = [["One" , 1] , ["Two" ,2] , ["Three" , 3] ] # list
e = {{"A" , 1} , {"B" , 1} } # set

print(dict(s)) # ValueError: dictionary update sequence element #0 has length 1; 2 is required
print(dict(d)) # {'A': 1, 'B': 2, 'C': 3}
print(dict(f)) # {'One': 1, 'Two': 2, 'Three': 3}
print(dict(e)) # TypeError: unhashable type: 'set'