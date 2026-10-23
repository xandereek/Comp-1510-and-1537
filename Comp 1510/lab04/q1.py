"""Lab 04, Question 1 -- Rock, Paper, Scissors Referee.

YOUR NAME
Complete decide_winner() and its docstring. Follow the lab handout.
"""


def decide_winner(player_one, player_two):
    """
    Determines the winner of a round of rock, paper, scissors.
    
    :param player_one: The move chosen by Player 1 ("rock", "paper", or "scissors").
    :param player_two: The move chosen by Player 2 ("rock", "paper", or "scissors").
    
    :return: A string indicating the outcome ("Player 1", "Player 2", or "Tie").
    """
    if not player_one == player_two:
        if (player_one == "rock" and player_two == "scissors") or (player_one == "scissors" and player_two == "paper") or (player_one == "paper" and player_two == "rock"):
            return "Player 1"
        else:
            return "Player 2"
    return "Tie"

def main():
    """Read both players' choices and display the result."""
    player_one = input("Player 1 choice: ")
    player_two = input("Player 2 choice: ")
    result = decide_winner(player_one, player_two)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
