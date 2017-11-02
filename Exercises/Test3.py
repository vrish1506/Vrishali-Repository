import sys
user1 = input("Your name ?")
user2 = input("And Your name?")

user1_answer = input("Do you want to choose rock, paper or scissors ?")
user2_answer = input("Do you want to choose rock, paper or scissors ?")

print(user1_answer)
print(user2_answer)


def compare(u1,u2):
   if u1 == u2:
      return("Its a tie")
   elif u1 == "rock" :
     if u2 == "paper":
        return("u1 rock wins")
     else:
        return("Not selected scissors win")
   elif u1 == "paper":
     if u2 == "scissors":
        return("u1 paper wins")
     else:
        return("Not selected rock wins")
   elif u1 == "scissors":
     if u2 == "rock":
        return("u1 scissors win")
     else:
        return("Not selected paper wins")
   else:
      return("Invalid input")
      sys.exit()


print(compare(user1_answer, user2_answer))

          
         
