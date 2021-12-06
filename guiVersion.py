import eel
#only one built in library
import urllib.request
#variable to keep track of the number of words converted
count = 0
#function that takes a pig latin string and converts it back to english
@eel.expose
def convertBack(pigLatin):
    global count
    count+=1
    #since there is no way to tell if the word started with a vowel or a consonant, we will perform both reversals and then compare with a dictionary
    #remove the 'ay' from the end of the word
    #remove the 'ay' from the end of the word and the last consonant to the beginning of the word

    attempt1, attempt2 = pigLatin[:-2], pigLatin[-3]+pigLatin[:-3]
    #returns attemp1 if the word is in the dictionary, otherwise returns attempt2
    url = f"http://wordnetweb.princeton.edu/perl/webwn?s={attempt1}"
    #open the url and read the html and see if the words 'any results' is in the html
    #this will tell us if the word is in the dictionary, so we return the correct word
    with urllib.request.urlopen(url) as response:
        html = response.read()
        return attempt2 if b'any results' in html else attempt1

#function that takes an argument and returns the string converted to pig latin
@eel.expose
def convertWord(word):
    global count
    count+=1
    #if the word starts with a vowel, add 'way' to the end of the word
    if word[0] in 'aeiou':
        return word + 'ay'
    #if the word starts with a consonant, move the first consonant to the end of the word and add 'ay'
    else:
        return word[1:] + word[0] + 'ay'

#function that returns the amount of words converted
@eel.expose
def returnWords():
    return count

eel.init('web')
eel.start('index.html')
