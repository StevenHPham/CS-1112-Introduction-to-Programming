
''' Purpose: Demonstrate notion of mappings -- using the if-elif-else structure
             Not recommended for large number of mappings
'''

reply = input( "Enter a Roman numeral: " )

roman_letter = reply.upper()

if   ( roman_letter == "I" ) :
    int_equivalent = 1
elif ( roman_letter == "V" ) :
    int_equivalent = 5
elif ( roman_letter == "X" ) :
    int_equivalent = 10
elif ( roman_letter == "L" ) :
    int_equivalent = 50
elif ( roman_letter == "C" ) :
    int_equivalent = 100
elif ( roman_letter == "D" ) :
    int_equivalent = 500
elif ( roman_letter == "M" ) :
    int_equivalent = 1000
else:
    value = None            #None means there is no value for it. A legal value for a variable

print( int_equivalent )
