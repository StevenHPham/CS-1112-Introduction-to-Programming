
''' Name: Steven Pham

    Email id: shp4df

    Purpose: get a positive number from the user; i.e., a number greater than zero
        if the user provides a zero or negative number, repeat the process
        until a positive number is gotten. Afterwards, perform a count down from
        the number to 0
'''

positive = True

while positive:
    reply = input("Enter a number greater than zero: ")
    r = int(reply)
    if r > 0 :
        positive = False

        for countdown in range(r, -1,-1):
            print(countdown)
