import random
guesses=0
num= random.randint(1,100)
user = 0
counter = 1
lowRange = (1)
highRange =(100)
while user!= num:
    user = int(input(f"Guess a number between {lowRange}  and {highRange}: "))
    if user >num:
        highRange=user
        user = print ("Too large.")
        guesses=guesses+1
    elif user<num:
         lowRange=user
         user = print("Too small.")
         guesses=guesses+1
    else:
          print(f"You got it. It only took, {guesses}, to get it correct")