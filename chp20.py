#######################################string ######################################################3
#number_one =input("enter your first number")
#number_two= input("enter your second number")
#total =number_one+number_two
#print(int(total))                                                                          # 45+45=4545


#number_one =input("enter your first number")
#number_two= input("enter your second number")
#total =int(number_one)+int(number_two)
#print(total)                                                                                   #45+45=90

#name,num =input("enter your name and number separated by comma : ").split(",")
#print(f"your name is: {name}")
#print(f"your rollno is: {num}")

name="anupam"
print(name[1])
print(name[-1])
print(name[0:5:2])       #start argument:stop arg :steps
print(name[::-1])  



lab="aman thapa"
print(len(lab))
print(lab.upper())
print(lab.lower())
print(lab.title())
print(lab.count("a"))


#strip method - remove spaces or something

name= "  guru     "
print(name.strip())              #lstrip and rstrip 




#find and replace method

string= "my name is hari is is is  "
print(string.replace("is","was",2))
print(string.replace("is","was",4))

first_is=string.find("is")
print(f"position of 1st \"is\" is {first_is}")
second_is= string.find("is",first_is +1 )
print(f"position of 1st \"is\" is {second_is}")
third_is= string.find("is",second_is +1 )
print(f"position of 1st \"is\" is {third_is}")



name= "harry"
print(name.center(9,"*"))

name =input("enter your name: ")
print(name.center(len(name)+8,"*"))


name="luis"
print(name.replace("u","t"))
print(name)                      # no change in original string,so strings are immutable








