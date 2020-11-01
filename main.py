#Amore' Daniels

#Your algorithm should go here OR you should use comments throughout
#Write a program that reads the file’s contents and calculates the
#average number of words per sentence.

#Open the file 
inFile = open('text.txt')

#Find the total amount of words in the file
#Read the file using the read method
content = inFile.read()
#Split the string to isolate words
words = content.split(' ')
#Initialize the variable
wordCounter = 0
#Count the number of words
for word in words:
    wordCounter += 1
    
#print(words)
print(wordCounter)

#Get the number of sentences by seperating at new line character
sentences = content.split('\n')
###Initialize the variable
##sentenceCounter = 0
###Count the number of sentences 
##for sentence in content:
##    sentenceCounter += 1

#Set variable to the amount of sentences in the content
numOfSentences = len(sentences)

#Find the average
avg = wordCounter//numOfSentences

#Print the average
print('Average words per sentence are {}.'.format(avg))

#Close the file
inFile.close()
