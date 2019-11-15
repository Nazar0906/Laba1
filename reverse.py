slogan=str(input('Enter word:' ))[::-1]
words= slogan.split()
slogan_rev = " ".join(reversed(words))
print(slogan_rev)