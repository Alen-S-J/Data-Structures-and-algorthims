import array



a=array.array('i',[1,2,3,4,5])

print("The array is:",end="")
for i in range(0,len(a)):
    print(a[i],end="")

print('\r')





print("The Popped Element is:",end="")
print(a.pop(2))



print("after operation:",end="")
for i in range(len(a)):
    print(a[i],end=" ")
