"""This function is used to remove the first occurrence of the value mentioned in its arguments. 
In this example, we are removing the first occurrence of 1 from a given array."""


import array

a=array.array('i',[2,3,4,1,6])


print("The array created is:",end="")
for i in range(0,len(a)):
    print(a[i],end="")

print('\r')

a.remove(6)

print ("The array after removing is : ",end="")
for i in range (len(a)):
    print (a[i],end=" ")