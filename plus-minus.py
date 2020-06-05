def plusMinus(arr):
    plusRatio = 0.00000
    minusRatio = 0.00000
    zeroRatio = 0.00000
    length = len(arr)
    for i in range(len(arr)):
        if arr[i]>0 :
            plusRatio += 1
        elif arr[i]<0 :
            minusRatio += 1
        else :
            zeroRatio += 1 
    print(plusRatio/length) 
    print(minusRatio/length) 
    print(zeroRatio/length)

n = int(input("enter number of elemnts "))
arr = list(map(int, input("enter array ").rstrip().split()))

plusMinus(arr)