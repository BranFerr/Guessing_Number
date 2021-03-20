#This is a guess the number game.
import random

def CheckWinner(_winner, _myName, _guess):
    if int(_winner) == 1:
       print('Good job, ' + str(_myName) + '! You guessed my number in ' + str(_guess) + ' guesses!')

    else:
       print('Sorry ' + str(_myName) + '! You DID NOT guess my number ')

#print('Hello! What is your name?')
myName = input('Hello! What is your name? ' )

number = random.randint(1, 20)
print('Well, ' + str(myName) + ', I am thinking of a number between 1 and 20.')

guessesTaken = 0
userGuess = 0
winner = 0

userGuess = int(input ('How many guesses would you like to have? ' ))

print ('')

while (guessesTaken < userGuess):
  print('Take a guess.') # There are four spaces in front of print.
  guess = int(input())

  if guess == number:
    winner = 1
  else:
    if guess < number:
        print('Too Low')
    elif guess > number:
        print('Too High')
  
  guessesTaken = guessesTaken + 1

  print('')
  print('You have taken ' + str(guessesTaken) + ' guesses.')

CheckWinner(winner, myName, guessesTaken)

#while 1:
# while (guessesTaken > userGuess):
#   print('Take a guess.') # There are four spaces in front of print.
#   guess = int(input())
#   #guessesTaken = guessesTaken + 1
#   if guess == number:
#     winner = 1
#     print('winner')
#     #break

#   else:
#      if guess < number:
#          print('Your guess is too low.') 

#      elif guess > number:
#          print('Your guess is too high.')

#   guessesTaken = guessesTaken + 1

# CheckWinner(winner, myName, guessesTaken)

####################################################################
