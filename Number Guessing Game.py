# Number Guessing Game
# USER HAVE 3 CHANCES TO GUESS IT!! 

chance = 3
secret_number = 8
count = 0

while chance > 0:
    guess = int(input("Enter number: ")) 
    print("*" * 50)

    if guess == secret_number:
        print("Congratulations, You win")
        print("*" * 50)
        count +=1
        break

    elif guess != secret_number and chance == 1:
        print("You lose")
        print("*" * 50)
        count += 1
        break

    else:
        if guess > secret_number:
            print("Hint: Secret number is smaller than your number")
            print("*" * 50)
        
        else:
            print("Hint: Secret number is greater than your number")
            print("*" * 50)

         
        print(f"You lose your {count + 1} chance")
        print("*" * 50)

        count += 1
        chance -= 1
    
print(f"You take {count} chance")