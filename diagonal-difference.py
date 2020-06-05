def diagonalDifference(arr):
    prim = 0
    sec = 0
    length = len(arr)
    for count in range(length):
        prim += arr[count][count]
        sec += arr[count][length-count-1]
    print (abs(prim - sec))

n = int(input("enter lenth of array ").strip())

arr = []
for _ in range(n):
        arr.append(list(map(int, input("enter array ").rstrip().split())))

diagonalDifference(arr)
