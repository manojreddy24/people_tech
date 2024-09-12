new_list=[1,2,"three",4.0]
print(new_list[0])
new_list.append(6)
new_list.insert(2,3)
print(new_list)
new_list.pop()#last element will be removed
print(new_list)
new_list.pop(2)#taking index as argument
print(new_list)
new_list.remove(4.0) #taking value as argument
print(new_list)
#copying list
new_list2=new_list.copy()
print("copied",new_list2)

new_list2.append(1)
print(new_list2.count(1))#counts the number of times 1 is present in the list
new_list2.reverse()#reverses the list
print("reversal",new_list2)
print("clear",new_list.clear())#clears the list
new_list2.remove("three")
new_list2.sort()#sorts the list
print("sorting",new_list2)
new_list2.extend([1,2,3])#adds the elements of the list to the end of the list
print("extended",new_list2)
print(new_list2.index(2))#returns the index of the first occurence of the element
print("slicing",new_list2[1:3])#slicing the list
print("traversing the list")
for i in new_list2:
    print(i)
print("while loop")
i=0
while i<len(new_list2):
    print(new_list2[i])
    i+=1
7325677378