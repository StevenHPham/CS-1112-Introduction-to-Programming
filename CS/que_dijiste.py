
''' Purpose: access the babelfish dictionary
'''

# get access to url support 
import url

# translation dictionary url -- entries are in csv form; i.e., word,translation
BABELFISH_URL = 'http://www.cs.virginia.edu/~cs1112/datasets/words/babelfish'

# get contents of babel fish url
word_mappings  = url.get_dataset( BABELFISH_URL )

# put entries into a dictionary - a mapping of words to translations
# the dictionary starts off empty

translation_dictionary = {}

# add each word-translation pair to the dictionary
for entry in word_mappings :
    # split entry into components and add mapping to the dictionary
    w, t = entry
    translation_dictionary[ w ] = t

# dump the dictionary

print( translation_dictionary )
