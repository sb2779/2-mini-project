# Apple , Strawberry , Banana are the object class of grocery


from Grocery import*

# Identities of all the fruits mentioned below including calories and price per kg
Apple = fruits('Kazakhstan','Red', 'No','Yes','it is not',73,'Aed 5')
Strawberry = fruits('Europe','Red','yes','No','Yes it is',33,'Aed 19')
Banana= fruits('Southeast asia','Yellow','No','No','it is not',89,'Aed 9')


# print apple,strawbeery,banana 
print('Apple     : '+ Apple.__str__())
print('Strawberry: '+ Strawberry.__str__())
print('Banana    : '+ Banana.__str__())
