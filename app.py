import random

def guess_number_game():
    # Start the game
    print("Welcome to the Number Guessing Game!")
    
    rounds = 0
    total_score = 0
    
    while True:
        # Generate a random number between 1 and 100
        target_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 10
        rounds += 1
        print(f"\nRound {rounds}:")
        print(f"You have {max_attempts} attempts to guess the number between 1 and 100.")
        
        while attempts < max_attempts:
            try:
                # Prompt the user to enter their guess
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            attempts += 1

            # Compare the guess with the target number
            if guess < target_number:
                print("Too low!")
            elif guess > target_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                total_score += (max_attempts - attempts + 1)  # Higher score for fewer attempts
                break
        else:
            print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {target_number}.")
        
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print(f"\nGame Over! You played {rounds} rounds with a total score of {total_score}.")
    return total_score

# Running the game (this won't take user input in this environment, but the function is ready for local use)
guess_number_game()
