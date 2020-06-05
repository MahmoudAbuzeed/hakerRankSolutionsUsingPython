def staircase(n):
       for i in range(n):
          result = ' '*(n-i-1) +('#')*(i+1)
          print(result)

  
n = int(input("enter the number "))

staircase(n)