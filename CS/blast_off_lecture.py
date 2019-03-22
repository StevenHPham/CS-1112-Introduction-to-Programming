
''' Purpose: prints a user-specified countdown followed by 'Blast off!'
'''


# get countdown range
reply = input( "Enter starting and ending numbers for the countdown: " )

high, low = reply.split()
high, low = int( high ), int( low )

# print off the range
for i in range( high, low - 1, -1) :
    print( i )

# print ending phrase
print( "Blast off!" )


accumulator = 0