
def bubble_sort(new_list):
    print("bubble_sort")
    #The outter loop controls the number of passes needed to sort everything
    for k in range(0,len(new_list)-1,1):
        #each pass of the bubble sorts one element. The number of passes needed are len(new_list)-1
            #the inner loop is moving the bubble along
        for i in range(0, len(new_list)-1,1):
            if new_list[i] > new_list[ i + 1]:

                temp = new_list[i]
                new_list[i] = new_list[i+1]
                new_list[i+1] = temp

def rbubble_sort(new_list):
    print("bubble_sort")
    #The outter loop controls the number of passes needed to sort everything
    for k in range(0,len(new_list)-1,1):
        #each pass of the bubble sorts one element. The number of passes needed are len(new_list)-1
            #the inner loop is moving the bubble along
        for i in range(0, len(new_list)-1,1):
            if new_list[i] < new_list[ i + 1]:

                temp = new_list[i]
                new_list[i] = new_list[i+1]
                new_list[i+1] = temp


new_list = [56,343,94,37,58,203,59,82]
print(new_list)
print("******************************")
bubble_sort(new_list)
print(new_list)
print("******************************")
rbubble_sort(new_list)
print(new_list)
print("******************************")












#get input to check
# input1 = int(input("Enter the first number: "))
# input2 = int(input("Enter the second number: "))
# input3 = int(input("Enter the third number: "))
# input4 = int(input("Enter the fourth number: "))
# input5 = int(input("Enter the fifth number: "))
# new_list = ["{0},{1},{2},{3},{4}".format(input1,input2,input3,input4,input5)]
#
#
# print(sort_accending(new_list))
