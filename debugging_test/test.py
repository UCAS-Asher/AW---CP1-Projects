import random
def start_game():
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    
    while not game_over:
        #It is a logic error, guess needed to be changed to an integer and this kept the game from working because it could not function because of the wrong data type.
        guess = int(input("Enter your guess: "))
        
        if guess == (1,100):
            continue
        else:
            print("Invalid Number")
            guess = int(input("Enter a guess in the number range 1-100: "))
        
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True

        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True

        # It was a logic error and attempts were not added when guess the was wrong which kept the player from losing the game.
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts += 1
        elif guess < number_to_guess:
            print("Too low! Try again.")
            attempts += 1  
        continue

    print("Game Over. Thanks for playing!")

start_game()