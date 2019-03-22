
''' Purpose: exercise module here_to_there
'''

import here_to_there

reply = input( 'Enter a Roman numeral: ' )

r = reply.strip() 

i = here_to_there.roman_to_int( r )

print( r, '=', i )

reply = input( 'Enter a word: ' )

w = reply.strip()

m = here_to_there.mapping( w )

print( w, '=', m )
