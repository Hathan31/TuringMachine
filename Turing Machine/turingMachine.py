#----------------------------------------- Turing Machine: Vending Beverage Machine -----------------------------------------------------
#----------------------------------------------- Jonathan Sampera Castellón -------------------------------------------------------------
#-------------------------------------------------- Theory of Computation ---------------------------------------------------------------
#This Turing Machine represents a Vending Beverage Machine that allows the user to select from three different beverages: Fanta ($2), Coke($5),
#and Sprite ($8). Each of the beverages has its own price, that is verified in the machine. User can be able to select the three beverages all
# at once, or just one or two. 
# --------------------------------------------------- Formal Defintion ------------------------------------------------------------------

# 1. Set of States = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'ACCEPTED', 'REJECT'}
# 2. Input Alphabet = {'F', 'C', 'S', '2', '5', '8'}
# 3. Tape Alphabet =  {'F', 'C', 'S', '2', '5', '8', 'E', 'X', 'Y', 'Z'}
# 4. Transition Function = 
# 5. Start State = q0
# 6. Accept State = ACCEPTED
# 7. Reject State = REJECT


#Define the transitions:
TRANSITIONS = {
    #State q0
    ('q0', 'F'): ('q1', 'F', 'R'),
    ('q0', 'C'): ('q2', 'C', 'R'),
    ('q0', 'S'): ('q3', 'S', 'R'),
    #State q1
    ('q1', '2'): ('q4', 'X', 'L'),
    #State q2
    ('q2', '5'): ('q5', 'Y', 'L'),
    #State q3 
    ('q3', '8'): ('q6', 'Z', 'L'),
    #State q4
    ('q4', 'F'): ('q7', 'X', 'R'),
    #State q5 
    ('q5', 'C'): ('q8', 'Y', 'R'),
    #State q6
    ('q6', 'S'): ('q9', 'Z', 'R'),
    #State q7
    ('q7', 'X'): ('q10', 'X', 'R'),
    #State q8
    ('q8', 'Y'): ('q10', 'Y', 'R'),
    #State q9
    ('q9', 'Z'): ('q10', 'Z', 'R'),
    #State q10
    ('q10', 'E'): ('ACCEPTED', 'E', 'R'),
    ('q10', 'F'): ('q1', 'F', 'R'),
    ('q10', 'C'): ('q2', 'C', 'R'),
    ('q10', 'S'): ('q3', 'S', 'R'),
}

# Define Turing Machine Logic.
def turing_machine(current_state, input_symbol):
    # Verify if the combination state-symbol is defined in the transitions
    if (current_state, input_symbol) in TRANSITIONS:
        # Get the new configuration according to the transitions
        new_state, write_symbol, move_direction = TRANSITIONS[(current_state, input_symbol)]
        # Return the new configuration
        return new_state, write_symbol, move_direction
    else:
        # If the configuration is not defined return REJECT.
        return 'REJECT', '', ''


# Function to execute the turing machine
def run_turing_machine(initial_state, tape):
    current_state = initial_state
    head_position = 0

    # Print the initial tape
    print("Initial Tape:", tape)

    while current_state != 'ACCEPTED' and current_state != 'REJECT':
        # Get the symbol under the reader's head
        current_symbol = tape[head_position]

        # Run the Turing machine for the current state-symbol combination
        new_state, write_symbol, move_direction = turing_machine(current_state, current_symbol)

        # Print the current state, tape, and the state it is transitioning to
        tape_with_head = [f"[{symbol}]" if i == head_position else symbol for i, symbol in enumerate(tape)]
        print(f"{current_state} {' '.join(tape_with_head)} {new_state}")

        # Write the new symbol on the tape
        tape[head_position] = write_symbol

        # Move the head of the reader in the direction indicated by the machine
        if move_direction == 'L':
            head_position -= 1
        elif move_direction == 'R':
            head_position += 1

        # If the reader head goes beyond the left edge of the tape, add a left edge
        if head_position < 0:
            tape.insert(0, 'E')
            head_position = 0

        # If the reader head goes beyond the right edge of the tape, add a right edge
        if head_position == len(tape):
            tape.append('E')

        # Update current status
        current_state = new_state

    # Print the final tape
    print("Final Tape:", tape)

    # Print the Result
    if current_state == 'ACCEPTED':
        print("The string was accepted.")
    else:
        print("The string was rejected.")

# Starting State
initial_state = 'q0'
# Input the string for the tape
tape_input = input("Welcome to our Vending Beverage Machine! Enter what beverages you will like: ")
# Initialize the Tape with the input string and an empty symbol at the end.
tape = list(tape_input) + ['E']

# Execute Turing Machine
run_turing_machine(initial_state, tape)
