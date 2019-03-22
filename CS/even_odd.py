
'''
    Purpose: introduction to dictionary'
'''

mappings = {}
mappings[ 1 ] = 'odd' 
mappings[ 2 ] = 'even' 
mappings[ 3 ] = 'odd' 
mappings[ 4 ] = 'even' 
mappings[ 5 ] = 'odd' 
mappings[ 6 ] = 'even' 
mappings[ 7 ] = 'odd' 
mappings[ 8 ] = 'even' 
mappings[ 9 ] = 'odd' 
mappings[ 'even' ] = 'a number is even if its remainder divided by 2 is 0'
mappings[ 'odd' ] = 'a number is odd if its remainder divided by 2 is 1'


reply = input( 'Enter a number: ' )
n = int( reply )

status = mappings[ n ]

print( n, status )

reply = input( 'Enter even or odd: ' )

meaning = mappings[ reply ]

print( meaning )
