# importing "array" for array operations
import array
	
# initializing array with array values
arr1 = array.array('i',[1, 2, 3, 1, 2, 5]) 
arr2 = array.array('i',[1, 2, 3]) 

# using extend() to add array 2 elements to array 1 
arr1.extend(arr2)

print ("The modified array is : ")
for i in range (0,9):
	print (arr1[i], end=" ")
