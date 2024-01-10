# R lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
textFile = open('sample.txt')
text = textFile.read()
textFile.close()

replacement = {}

replacement["ADJECTIVE"] = input("Enter an adjective ")
replacement["NOUN"] = input("Enter an noun ")
replacement["VERB"] = input("Enter an verb ")
replacement["adverb"] = input("Enter an adverb ")

for code,word in replacement.items():
    text = text.replace(code,word)

textFile = open('output.txt','w')
textFile.write(text)
textFile.close()