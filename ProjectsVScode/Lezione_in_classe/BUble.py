def bubble_sort(x):
    for _ in range(len(x)):
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
                temp=x[j]
                x[j] = x[j+1]
                x[j+1]=temp
l=[1,2,3,4,5,6,7,8,9,0]
bubble_sort(l)
print(l)        