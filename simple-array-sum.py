
def simpleArraySum(ar):
   
    sum = 0
    for element in ar :
        sum+= element
    print(sum) 



ar_count = int(input("enter the nummber "))

ar = list(map(int, input("enter the array ").rstrip().split()))

simpleArraySum(ar)

    