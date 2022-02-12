l = []
n = int(input())
for i in range(0, n):
    ele = int(input())
    l.append(ele) 
def insertion_sort(list):
    
    for index in range(1,len(list)):
        value=list[index]
        i=index-1
        while i>=0:
            if value < list[i]:
                list [i+1] = list[i]
                list[i]=value
                i=i-1
            else:
                break

insertion_sort(l)
print(l)