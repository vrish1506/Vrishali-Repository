import random
import pytest


MIN = 1
MAX = 9 

NUMBER = random.randint(MIN, MAX)

GUESS = None
ANOTHER = 0
TRY = 0
RUNNING = 1 

print "Alright..." 

while RUNNING:
  GUESS = raw_input("What is your lucky number? ")
  
  if int(GUESS) < NUMBER:
    print("Wrong, Too low") 
  elif int(GUESS) > NUMBER:
    print("Wrong, Too High")
  elif GUESS.lower() == "exit":
    print("Exiting")
  elif int(GUESS) == NUMBER:
    print "Yes, thats the one %s." % str(NUMBER)
    if TRY < 2 :
      print("Impressive, tries just less than %s." % str(TRY))
    elif TRY > 2 and TRY < 10:
      print("Still good less than 10 tries %s tries"  % str(TRY))
    else:
      print("Bad, so many tries")

    RUNNING = 0

  TRY += 1

   
