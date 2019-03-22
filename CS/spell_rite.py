
''' Purpose: produce spell-check corrected text
'''

# get access to url support
import url

# CS 1112 most common words
MOST_COMMON_URL = 'http://www.cs.virginia.edu/~cs1112/words/most-common'

# CS 1112 words correctsions CSV
CORRECTIONS_URL = 'http://www.cs.virginia.edu/~cs1112/words/corrections.csv'

# get contents of most common words url
spellings = url.get_text( MOST_COMMON_URL )

# get contents of corrections url
dataset = url.get_dataset( CORRECTIONS_URL )

# get the user text to be checked
reply = input( 'Enter text: ' )

# convert reply into a list of words
text = reply.split()

# what now ???

#Step1: build a dictionary from the dataset
dict = {}

for row in dataset:
    wrong, right = row
    #assign the value of right spelling to the key wrong spelling
    dict[wrong] = right

    u1 = wrong.upper()
    u2 = right.upper()
    dict[u1] = u2

    c1 = wrong.capitalize()
    c2 = right.capitalize()
    dict[c1] = c2

#split does not belong to list
spellings = spellings.split()

#step 2: split giant string (spellings) into an actually list


#step3: be able to handle different word cases

all_spellings = []
for word in spellings:
    cword = word.capitalize()
    uword = word.upper()
    all_spellings.append(word)
    all_spellings.append(cword)
    all_spellings.append(uword)

output = ''
for word in text:
    if word in all_spellings:
        output = output + word + ' '
    elif word in all_spellings:
        correction = dict[word]
        output = output + '*' + correction + '*'
    else:
        output = output + "?" + word + '?'

print(output)

