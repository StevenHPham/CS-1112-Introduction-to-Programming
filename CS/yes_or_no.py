
''' Purpose: repeatedly prompt the user until they reply with a yes
        or no. The case of the letters do not matter.
'''

looking_for_a_yes_or_no = True

while ( looking_for_a_yes_or_no ) :
    reply = input( 'Enter (yes / no): ' )
    reply = reply.lower().strip()
    if reply in ([ 'yes', 'no' ] ):

       looking_for_a_yes_or_no = False

print( reply )
