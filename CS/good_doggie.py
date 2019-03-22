
''' Purpose: demonstrate dict mappings
'''

# get access to url support
import url

# where is the dog to notoriety mappings
PUPPIES_CSV = 'http://www.cs.virginia.edu/~cs1112/datasets/csv/puppies.csv'

# get data set
dataset = url.get_dataset( PUPPIES_CSV )


# convert dataset to a form suitable for querying

notoriety =  { }

for row in dataset :
    name, fame = row
    notoriety[ name ] = fame
    print(row)

# ask for dog of interest
reply = input( 'Enter name of dog: ' )

dog = reply.strip()
dog = dog.capitalize()

# look up claim to fame

fame = notoriety.get( dog )

print( fame )
