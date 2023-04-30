string = input("Enter a String : ")
string = string.lower()
li = []
for i in string:
    if i not in li:
        li.append(i)
    else:
        pass
str = (",").join(li)
print(str)