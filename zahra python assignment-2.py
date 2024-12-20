# 1.program to add 'giraffe 'at the end of given list
animalList=['Fox','Lion','Horse','Zebra']
animalList.append('Giraffe')
print(animalList)

#2.program to create a tuple of numbers using tuple constructor
tup=tuple((11,12,13,14,15,16,17,18,19,20))
print(tup)

#3.program to print the index of 'black' and 'yellow' from the below given list
colorList=['blue','red','pink','black','green','yellow']
print(colorList.index('black'))
print(colorList.index('yellow'))

#4.Adding new key Madhya Pradesh,and value Bhopal, and removing the key Rajasthan and its value in the given dictionary
Places={'Maharashtra':'Mumbai','Rajasthan':'Jaipur','Tamil Nadu':'Chennai'}
Places.update({'Madhya Pradesh':'Bhopal'})
Places.pop('Rajasthan')
print(Places)

#5.program to add [10,20,30] as a list at the end of the given list
numList=[1,2,3,4,5]
numList2=[10,20,30]
output=numList+[numList2]
print(output)

#6.program to print elements of the below tuple from 'Laptop' to 'Headphones'
items=('Mobile Phone','Earphones','Laptop','Bluetooth Speaker','Writing Pad','Headphones','Smart Watch','Digital Camera')
print(items[2:6])

#7.program to print the keys and values separately of the dictionary,also converting the values into the list and print the new list
marksDict={'Tom':98,'Sam':78,'Pam':63,'Tony':82,'Brian':91}
print(marksDict.keys())
print(marksDict.values())
newList=list(marksDict.values())
print(newList)

#8.given below is a dictionary
fruits={'orange':5,'cherry':10,'banana':6,'guava':7,'apple':8}

#(a)update the value of guava with double of its current value
fruits.update({'guava':14})
print(fruits)
#(b)update the value of orange with 5 minus the square of its current value
fruits.update({'orange':-20})
print(fruits)

#9.Given a list A and tuple B ,update the last element of listA with last element of tupleB and vice versa
A=[10,20,30,40,50]
B=(1,2,3,4,5)
A[4]=5
print(A)
#since tuples are immutable, we will convert the tuple into list to change the last element
tupList=list(B)
tupList[4]=50
#converting the list into tuple
B=tuple(tupList)
print(B)

#10.We are given three sets
setA={1,5,2,6,3,7,4}
setB={6,7,8,9,10}
setC={4,5,11,2,10,9}
#(a)setB-setA-setC
diff=(setB-setA-setC)
print(diff)
#(b)union between setA and setB
print(setA.union(setB))
#(c)intersection between setA and setC
print(setA.intersection(setC))
