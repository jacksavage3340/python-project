list_1=[1,9,2,4,5,7,6]
list_2=[10,12,15,17,91,22]
combined_list=list_1+list_2
even=[]
odd=[]
for i in combined_list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort()
final_list=even+odd
print("list 1",list_1)
print("list 2",list_2)
print(final_list)