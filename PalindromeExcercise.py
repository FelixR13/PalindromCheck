from inspect import Traceback
import string
import sys

"""

Palindrom-Check von FelixR

"""
run=True
while run==True:
    word=input("Insert Word or Name: ")                         #prints the input message 
    flag=False
    wordOriginal=word                                           #saves the original input for the output
    wordLength=len(word)                                        #gets the word length


    if any(char.isdigit() for char in word):                    #checks if any numbers are in the input
        print("No Numbers allowed") 
        continue
              
    elif word=="" or len(word)==0:                              #checks if any inputs are made
        print("Error! No text recognized!")   
        continue  
    
    elif len(word)<=2 :                                         #checks if the word is longer than 2 char
        print("Text is to short! ") 
        continue

    elif any(char in string.punctuation for char in word):      #checks if any symbols are used
        print("No symbols allowed")
        continue

    else:
        word=word.lower()                                       #lowers the letters to compare it with the wordBackward variable
        wordBackward=""
        for i in range (wordLength-1,-1,-1):                    #inverts the original word by adding the last char first and counting down from the wordLength
            wordBackward=wordBackward+word[i]
        if word == wordBackward:                                #compares the orginal word and the word spelled backwards with each other
            flag=True
        print (wordOriginal+" is a palindrome = "+str(flag))    #prints the result 
    while True:
        nextWord=input("Check another Name or Word? (Y/N)")
        if nextWord =="Y" :
            break
        if nextWord =="N":
            print(1)
            sys.exit()
        else:
            print("Invalid input")
            continue
    continue   


    
