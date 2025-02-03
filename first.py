#this program about create list and multipy each index of the list
lst=[]
n=int(input("Enter number: "))
for i in range(n):
    data=int(input("Enter data elements: "))
    lst.append(data)
print(lst)

x=1
for i in lst:
    x=x*i
print(x)
