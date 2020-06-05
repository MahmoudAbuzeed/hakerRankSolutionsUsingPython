def birthdayCakeCandles(ar):
    count = 0
      # 3 2 1 3
    big = max(ar)
    for i in range (len(ar)):
        if ar[i]==big:
            count +=1
    print(count)

ar_count = int(input("enter array count "))

ar = list(map(int, input("enter array ").rstrip().split()))

birthdayCakeCandles(ar)
