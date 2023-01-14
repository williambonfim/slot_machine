# Slot Machine

The following code is a simulation of a slot machine game. It starts by importing the `random` library, which is used to randomly select symbols for the slot machine. The program then defines several constants, including the maximum and minimum bets allowed, the number of rows and columns for the slot machine, and dictionaries that store the number and value of each symbol.

The `check_winnings` function takes four arguments: the columns of the slot machine, the number of lines bet on, the bet amount, and the value of each symbol. It calculates the winnings for the player by comparing the symbol in the first column of each line to the symbols in the rest of the columns. If all symbols match, the winnings are incremented by the bet amount multiplied by the value of that symbol. The function also keeps track of the winning lines.

The `get_slot_machine_spin` function takes three arguments: the number of rows and columns for the slot machine, and the symbols to be used. It creates a 2D list that represents the columns of the slot machine and fills it with randomly chosen symbols.

The `print_slot_machine` function takes one argument: the columns of the slot machine. It iterates through each row and column of the slot machine and prints the symbol at that location.

The `deposit` function prompts the user to enter the amount they would like to deposit, and only returns the amount if it is a positive number.

The `get_number_of_lines` function prompts the user to enter the number of lines they would like to bet on, and only returns the number if it is within the allowed range.

The `get_bet` function prompts the user to enter the amount they would like to bet on each line, and only returns the amount if it is within the allowed range.

The `spin` function takes one argument: the player's balance. It calls the `get_number_of_lines`, `get_bet`, and `get_slot_machine_spin` functions to get the user's bet, the number of lines bet on, and the slot machine spin. It then calls the `check_winnings` function to calculate the winnings and prints the result. The function returns the difference between the winnings and the total bet.

Finally, the `main` function is called, which initializes the player's balance and enters a loop that allows the player to play until they choose to quit. It calls the `deposit` function to get the initial deposit and enters a loop that allows the player to play the slot machine using the `spin` function until the player chooses to quit or their balance becomes zero.
