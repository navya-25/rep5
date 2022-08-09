lst=[]
for i in range(1,5):
    a = int(input())
    lst.append(a)
print(lst)
min = lst[0]
for i in range(1,5):
    if(lst[i] < min):
        min = lst[i]
print(min)
