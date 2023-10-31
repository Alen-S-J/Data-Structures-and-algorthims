import array
a = array.array('i', [1, 2, 3]) 
 
# printing original array
print ("The new created array is : ",end=" ")
for i in range (0, 3):
    print (a[i], end=" ")
print('\r') 

a.append(9)

print("The append array is : ",end="")
for i in range (len(a)):
    print(a[i],end=" ")
