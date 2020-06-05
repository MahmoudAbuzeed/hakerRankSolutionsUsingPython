def timeConversion(s):
    amOrPm = s[-2:]
    time = ""

    if(amOrPm == "PM"):
        if(int(s[0:2]) < 12):
            time = time + str(12 + int(s[0:2])) + s[2:-2]
        else:
            time = time + str(int(s[0:2])) + s[2:-2]
    else:
        if(s[0:2] == '12'):
            time = time + "00" + s[2:-2]
        else:
            time = time + s[:-2]

    print (time)

s = input("enter the time ")

timeConversion(s)
