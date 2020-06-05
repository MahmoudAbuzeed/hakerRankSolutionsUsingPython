def aVeryBigSum(ar):
    sum = 0
    for n in range(len(ar)):
        sum+=ar[n]
    print (sum)    

ar_count = int(input("enter the array count "))

ar = list(map(int, input("enter the array ").rstrip().split()))

aVeryBigSum(ar)