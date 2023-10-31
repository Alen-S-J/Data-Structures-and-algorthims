# importing "array" for array operations
import array
	
# initializing array with array values
arr = array.array('i',[1, 2, 3, 1, 2, 5]) 

# using tolist() to convert array into list
li2 = arr.tolist()

# printing the new list
print ("The new list created is : ",end="")
for i in range (0,len(li2)):
	print (li2[i],end=" ")
