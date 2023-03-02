strr = input("Enter a string: ")
li = []
ll = []
for i in strr:
    if i not in li:
        li.append(i)
    else:
        ll.append(i)
print(strr)
print(ll)
