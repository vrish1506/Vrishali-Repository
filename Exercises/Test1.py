
import random 
string = input("Enter a string : ")
length = len(string)
print(length)
for i in range(length):
 print("i: =", i)
 if (string[::1] == string[::-1]):
   value = 0 
   break
 else:
   value = 1 
   break
 
print(value)
if (value == 0):
  print("Palin")
else:
  print("No Palin")

   
 



