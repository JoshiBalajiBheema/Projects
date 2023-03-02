#This code can be upgraded with While loop for more interarction and also could add dictionaries.

list = ["apples", "oranges", "grapes"]
print('Items in list : ',list)
print()
c = input("What would you want to do? ADD/REMOVE? ").lower()
c1 = ['add']
c2 = ['remove']
c3 = c1+c2

if c not in c3:
    print("Not a valid command. ")

if c in c1:
    addItem = input("Add Item : ")
    if addItem not in list:
        list.append(addItem)
        print(list)

if c in c2:
    removeItem = input("Remove item : ")
    if removeItem in list:
        list.remove(removeItem)
        print(list)
    if removeItem not in list:
        print('The item is not in the list')
        print("None of the items removed.")
        print('Current items in list : ',list)
