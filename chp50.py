###########################         list          #################################

misc =["hari","pandey",1,2,3,6.7,"golmaal"]
print(misc[1])
print(misc[0:2])
misc[1]="joshi"
print(misc)

# append,insert,extend,                   # pop,delete , remove 

fruits=["apple","pineapple","mango"]
fruits.append("banana")      # add at last position 
print(fruits)
fruits.insert(2,"grapes")     # add at specified position
print(fruits)
fruits.pop()                   # delete last position of list  .pop(1),.pop(2)
print(fruits)
fruits.reverse()                # reverse 
print(fruits)
del fruits[2]                     # delete operator
print(fruits)
fruits.remove("apple")                 # remove that specified word 
print(fruits)


fruits = []
a=input("enter a fruit name: ")
fruits.append(a)
print(f"your fruit is {fruits}")

# concatenate 
list1 =[ "apple","ball","cat","dog"]
list2 =["egg","fog","girl"]
list3 = list1+ list2
print(list3)
 # or 
list1.extend(list2)
print(list1)
list1.append(list2)  # list inside list 
print(list1)

