def main():
    time = input().split(":")
    time[0] = int(time[0]) #totally inefficient

    if time[2][2] == "P":
        if time[0] < 12:
            time[0] = time[0] + 12
        time[0] = str(time[0])
    elif time[0] < 10:
        time[0] = "0" + str(time[0])
    elif time[0] == 12:
        time[0] = "00"
    else:
        time[0] = str(time[0])        
    
    time = ":".join(time)
    print(time[:-2])

main()

### Messed up my solution

##here is the editorial:
# s = raw_input()
# zn = s[-2:]
# if zn == "PM" and s[:2] != "12":
#     s = str(12 + int(s[:2])) + s[2:]
# if zn == "AM" and s[:2] == "12":
#     s = "00" + s[2:]
# print s[:-2]