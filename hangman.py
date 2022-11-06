#hangman

import time

def hangman(word):
    wrong = 0
    stages = [" _______ ", "  | ", "  |  | ", "  |  0 ", "  | /|\ ", "  | / \ ", "__|__ " ] 
    rletters = word.lower() 
    guess = '-'*len(word)

    i=0
    while wrong<=len(stages):
        letter = input('enter your guessing letter: ').lower()
        if letter in rletters:
            position = rletters.index(letter)
            #rletters.replace(position,letter) #this is for non repeated letters
            #guess[position] = letter
            rletters = rletters[:position] + "_" + rletters[position + 1:]
            guess = guess[:position] + letter + guess[position + 1:]
            print(guess)
            if guess==word:
                time.sleep(1)
                print('\nYou are win!...\n')
                break
        else:
            try:
                for j in range(i+1):
                    print(stages[j])
            except:
                print(f'you are hanged try again...\n')
                break
            i+=1
            wrong += 1   

           
for i in "Welcome to Hangman Game":
    print(i,end='')    #print welcome board slowly in horizontally
    time.sleep(0.2) 
print('\n')
word = input('enter a secret word :')
hangman(word)
