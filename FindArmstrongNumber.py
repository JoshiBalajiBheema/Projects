x = input("Enter a number to find if its an ARMSTRONG number OR not : ")
n = len(x)
k = 0
arm_list = []
for i in x:
    arm_gen = (int(x[k]) ** n)
    arm_list.append(arm_gen)
    k += 1
arm_sum = sum(arm_list)
print(arm_list)
x = int(x)
if x == arm_sum:
    print(f"This is an ARMSTRONG NUMBER with 'order {n}'")
    print(f"Your input : '{x}'\nArmstrong Number : '{arm_sum}'")
else:
    print("Not an Armstrong Number")
 
