def stutter(word):
    truncword = word[0] + word[1]
    print(truncword + "..." + truncword + "..." + word + "?")

word = input("Enter a word: ")
stutter(word)
