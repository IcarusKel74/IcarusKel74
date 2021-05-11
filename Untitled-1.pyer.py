name_var = input("Name Please?")
 
if (name_var.find("w") == len(name_var) -1):
    print("Found")


 
def add_nums(first, Second):
    return first + Second
 
result = add_nums(1, 2)
 
print(result)
 
if (name_var == "Matt"):
    print("Hi Matt")
 
else:
    print("Who tf is " + name_var)
 
if (name_var.find("M") != -1):
    print("M was found")
 
if (name_var == "Matt"):
    print("Hi Bro!")
 
elif (name_var == "Daniel"):
    print("Hi Dan bro")
 
elif (name_var == "Annie"):
    print("Hey Annie Sis")
 
else:
    print("Hi dude")
 
y = {"1", "2", "3"}
 
for x in y:
    print(x)