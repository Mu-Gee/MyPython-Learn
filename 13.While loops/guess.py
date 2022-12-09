# Let's build a guessing game with a while loop
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
     guess = int(input('Guess: '))
     guess_count += 1
     if guess == secret_number:
         print("You won")
         break
# This executes if all the conditions above fail
else:
    print("Sorry you failed")
