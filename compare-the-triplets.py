def compareTriplets(a, b):
    x=0
    y=0
    for element in range(3):
        if a[element]>b[element]:
            x+=1
        elif a[element]<b[element]:
            y+=1
    print(x, y) 

a = list(map(int, input("enter the first list ").rstrip().split()))

b = list(map(int, input("enter the second list ").rstrip().split()))

compareTriplets(a, b)