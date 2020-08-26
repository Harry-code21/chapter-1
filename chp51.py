fruits = ['apple', 'pineapple', 'grapes', 'mango', 'banana']
if "apple" in fruits:
    print("True")
    


fruits = ['apple', 'pineapple', 'grapes', 'mango', 'banana']
a=input("enter any fruits to check whether it is in list or not : ")    
if a in fruits:
    print("present")
print("not present ")    


print(fruits.count("apple"))     # count 
fruits.sort()
print(fruits)

num=[1,4,5,45,657,2,234,67,89]
num.sort()
print(num)
print(sorted(num))    # no change in original list 
num_copy= num.copy()
print(num_copy)
num3=num+num_copy             # concatenate method 
print(num3)


list1= [1,2,3,4,5]
list2=[1,2,3,4,5]
print(list1 == list2)      # compares only data 
print(list1 is list2)  