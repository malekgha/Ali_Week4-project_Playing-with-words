
### Setup Section ###

# We'll learn about how this line of code works later in the course - for now just know it loads the colored text
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy#############################################################################
def printGuessAccuracy(guess, actual):

  secret = "spring"
  # Loop through each index/position 
  for index in range(6):

    guess = input("Enter a six-letter word: ")
    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if letter in secret:

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == secret[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:
        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True, False )

    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      printColorfulLetter(letter, False, False)
      
    # Don't worry about the line of code below, it works. It just handles the transition between colors
    print(Style.RESET_ALL + " ", end="")

    

# TO-DO: Write a Function that takes in a six-lettered word from the user
#############################################################################################
def getSixLetterInput(guess):

  guess = " "
  while len(guess) != 6:
    return guess
   
    guess = input("Enter a six letter word: ")
  print(getSixLetterInput(guess))

# This marks the end of the function definitions, below this is where the program will actually start!

### Main Program ###




# This marks the end of the function definitions, below this is where the program will actually start!




################################### Main Program ###################################
# TO-DO: Write the logic of the game here!

#Dispaly a friendly title using ASCII art generator. Just copy and paste your word between three qutation marks
#https://patorjk.com/software/taag/#p=display&f=Big%20Money-se&t=Quiz%20Time!
print(""" 

               U  ___ u   ____     ____         ____      _         _      __   __ 
 __        __    \/"_ \/U |  _"\ u |  _"\      U|  _"\ u  |"|    U  /"\  u  \ \ / / 
 \"\      /"/    | | | | \| |_) |//| | | |     \| |_) |/U | | u   \/ _ \/    \ V /  
 /\ \ /\ / /\.-,_| |_| |  |  _ <  U| |_| |\     |  __/   \| |/__  / ___ \   U_|"|_u 
U  \ V  V /  U\_)-\___/   |_| \_\  |____/ u     |_|       |_____|/_/   \_\    |_|   
.-,_\ /\ /_,-.     \\     //   \\_  |||_        ||>>_     //  \\  \\    >>.-,//|(_  
 \_)-'  '-(_/     (__)   (__)  (__)(__)_)      (__)__)   (_")("_)(__)  (__)\_) (__) 


""")
#add space
print()
#add a welcoming message:
print("Welcome to Word Play! ")
#add space
print()
#separate the header section from the play's description using a line of continuous equal signs
print("======================================")
print()
#add a space
print()
#add the play's description below
print("You have five tries to get the word correct")
print("The word is FIVE CHARACTERS long, and you must enter a guess of this length")
print("If a letter is in the correct palce, it will be green")
print("If a letter is in the word but NOT in the correct place, it will be yellow")
print("If the letter is NOT in the word, it will be red")


#Repeat the player's turn until they either run out of tries or guess the word correctly



#On each turn, take in a word, and show them how accuaret it was



#When they've finished, tell them if they won or lost