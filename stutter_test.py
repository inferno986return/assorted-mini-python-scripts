##def stutter(word):
##	stutter = word[0] + word[1]
##	print(stutter + "... " + stutter + "... " + word)
##	return word

def stutter(word):
	stuword = word[0] + word[1]
	print(stuword + '... ' + stuword + '... ' + word + '?')
	return word
    
word = "increasing"
stutter(word)
