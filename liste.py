 #Sum of numbers
list = [43,54,23,95,93]  #list or array
arraytotal = 0   #set total to 0 before any operations
for index in range(0,len(list)): #we want the sum of all the indices so 0 - len(list)
    arraytotal += list[index]

print("**********SUM**************")
print(arraytotal)
print("************SUM************")


 #print the largest number:
highest = max(list) #max function gives largest number in the "list" array
print('**********LARGEST_NUMBER**************')
print(highest)
print("**********LARGEST_NUMBER**************")
#or withouth using built in function
max= 0
for i in list:
    if i > max:
        max=i
print("**********LARGEST_NUMBER**************")
print(max)
print("**********LARGEST_NUMBER**************")

#print the Smallest number:
minimum = min(list) #min function gives smallest number in the "list" array
print("**********SMALLEST_NUMBER**************")
print(minimum)
print("**********SMALLEST_NUMBER**************")
#or
min_num = list[0]

for i in range(1,len(list)):
    if list[i] < min_num:
        min_num = list[i]

print("**********SMALLEST_NUMBER**************")
print(min_num)
print("**********SMALLEST_NUMBER**************")
