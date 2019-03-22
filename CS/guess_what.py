
''' Purpose: play guess a number
'''

# specify max number
n = 10000

# start the game
'''print( 'Think of a number from 0 to', n )

# ???
for i in range(1, 100001):
    print("is it ", i)

    prompt = "is it " + str(i) + ' : '
    reply = input(prompt)
    reply = reply.strip().lower()

    if reply == 'yes' :
        print("I got it")
        '''

looking_for_number = True
next_guess = 1

while (looking_for_number):
    prompt = "is it " + str(next_guess) + ' : '
    reply = input(prompt)
    reply = reply.lower().strip()

    if reply == 'yes':
        print("I got it!")
        looking_for_number = False
    else:
        next_guess = next_guess + 1

