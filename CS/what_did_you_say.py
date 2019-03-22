
''' Purpose: translate user text to English
'''

# get access to url support
import url

# CS 1112 translation dictionary -- entries are of form: word,translation
BABEL_FISH_URL = 'http://www.cs.virginia.edu/~cs1112/words/babelfish'

# get contents of babel fish url
dataset = url.get_dataset( BABEL_FISH_URL )

# convert csv-based word mappings into dictionary format
word_mappings = {}

for row in dataset:
    w1,w2 = row
    word_mappings[w1]=w2

# get the user text to be translated
reply = input( 'Enter phrase to be translated: ' )

# convert reply into a list of words
to_be_translated = reply.split()

# process the list word by word -- that is, build up the output phrase
#     word by word
sentence = ""                   #We initialize our accumulator to be an empty string so that we can translate each word as we go and add it to our big string of translated word

for word in to_be_translated :
    # translate word
    word = word.lower()
    if word in word_mappings:
        translation = word_mappings.get(word)
    else:
        translation= '>' + word + '<'
    sentence = sentence + translation + ' '
print(sentence)

# print translation t
