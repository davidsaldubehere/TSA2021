from PyDictionary import PyDictionary

dictionary=PyDictionary()
count = 0
#function that takes a pig latin string and converts it back to english
def convertBack(pigLatin):
    global count
    count+=1
    #since there is no way to tell if the word started with a vowel or a consonant, we will perform both reversals and then compare with a dictionary
    #remove the 'ay' from the end of the word
    #remove the 'ay' from the end of the word and the last consonant to the beginning of the word

    attempt1, attempt2 = pigLatin[:-2], pigLatin[-3]+pigLatin[:-3]
    #returns attemp1 if the word is in the dictionary, otherwise returns attempt2
    return attempt1 if not dictionary.meaning(attempt1,True) is None else attempt2

#function that takes an argument and returns the string converted to pig latin
def convertWord(word):
    global count
    count+=1
    #if the word starts with a vowel, add 'way' to the end of the word
    if word[0] in 'aeiou':
        return word + 'ay'
    #if the word starts with a consonant, move the first consonant to the end of the word and add 'ay'
    else:
        return word[1:] + word[0] + 'ay'

#continuously ask if the user wants to convert a word to pig latin until the user responds no
while True:
    #ask the user for a word
    userInput = input('Enter a word to convert to pig latin: \nIf you want to stop, type "stop"\nIf you want to convert pig latin back to english, type "back"\n')
    #if the user responds no, break out of the loop
    if userInput == 'stop':
        break
    #if the user responds back, print the pig latin word coverted back to english
    elif userInput == 'back':
        print('The english word is:', convertBack(input('Enter a pig latin word to convert back to english: ')))
        print('\n')

    else:
        print(convertWord(userInput))
        print('\n')
#print the total number of words converted ensuring that the plural is correct
if count == 1:
    print(f'You converted ' + str(count) + ' word')
else:
    print(f'You converted ' + str(count) + ' words')