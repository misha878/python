# create a class with a class attribute a; create an object from it and set 'a'
# directly using object,a=o.does this change the class attributeemo:

class Deom:
    a = 4
    
o = Deom()
print(o.a) # print the class attributee attribute is not present becaue instance
o.a = 0 # instance attribute is set     
print(o.a) # print the class attributee attribute is  present becaue instance
print(Deom.a) # print the class attributt