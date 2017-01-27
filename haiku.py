# Generate a haiku with punctuation for emphasis in and between lines

from random import shuffle
import random

# How many Es instead of syllables for now (note to self)
# This top section is trying to pick a random word from the list of strings

shuffle(x) # This is bad; `print x` only returns 0
    
# print(random.choice(splitsy)) # Does this work? Yeeee

# Now we're defining some things

f = open("/usr/share/dict/words", "r")
text = f.read()
splitsy = text.split('\n')

def randomword():
	f = open("/usr/share/dict/words", "r")
	text = f.read()
	splitsy = text.split('\n')
	shuffle(splitsy)
	return splitsy[0]
	
str = randomword()
eees = str.count('e')
# do the loop in the juup
# get the word
# printing is where the syllable word exclusion happens
# put python notebook on da github???


	

# Count number of syllables
def syllable(string):
	return 1
	
# And then the decrement loop stuff is down here

# Not gonna use this but:
# for i in range(5, 1, -1):

# Or we could try a while loop?
# while(

#Or maybe this is relevant?
# def remove_doubles(old):
#    new = []
#    for item in old:
#        if new and item == new[-1]:
#            continue
#        new.append(item)
#    return new

# Do something with text here, like:
for word in splitsy: # Or maybe for (random.choice(splitsy))? Would that work?
	if syllable(word) > 5: # Make this make sense, not counting length.
		# How do I skip and pick a new word
		# How do I randomly get a word from the list? Check.
		
# count = syllable(splitsy) Is this smart?
	
	elif len(syllable) == 5:
	# Print it?
	
	elif len(syllable) == 4:
	# Better way to decrement than actually just counting down like this?
	
	
	
	else:
	
# Now something for shuffle

