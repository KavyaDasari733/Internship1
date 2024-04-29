import random

def get_user_choice():
    """Prompt the user to choose rock, paper, or scissors."""
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    """Generate a random choice (rock, paper, or scissors) for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's choice and the computer's choice."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\n--- Rock, Paper, Scissors ---")
        
        # Get user and computer choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        # Display choices
        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)
        
        # Determine the winner and display result
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        # Display scores
        print("Your score:", user_score)
        print("Computer's score:", computer_score)
        
        # Ask user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
