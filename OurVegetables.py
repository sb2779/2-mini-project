# Brinjal , Tomato , Broccoli are the object class  

from Vegetables import*

# Identities of all the vegetables including calories in kcal and price per kg
Brinjal = Vegetables('India','Purple','Yes', 'Root',25,'Bitter','Aed 8')
Tomato =  Vegetables('America','Red','No', 'Stem',22,'Tarty','Aed 6')
Broccoli= Vegetables('Asia','Green','Yes', 'Stem',33,'Grassy','Aed 9')

# print brinjal,tomato,broccoli

print('Brinjal :'+ Brinjal.__str__())
print('Tomato  :'+  Tomato.__str__())
print('Broccoli:'+ Broccoli.__str__())


