def main():
    pass


def prompt(valid_inputs, help_string):
    """Prompts the user to make an input choice. If the choice is not in
    the provided list of valid inputs, the user is prompted for a new choice.
    At any time the user can enter '?' which will display the provided help
    text contained in help_string.
    Inputs:
        valid_inputs - list of inputs to accept
        help_string - provided help text with a details on each of the options
    Output:
        A valid choice from valid_inputs provided by the user"""
    input_received = False
    while not input_received:
        choice = input("> ").lower()
        if choice in valid_inputs:
            input_received = True
        elif choice == "?":
            print(help_string)
            print()

    return choice


if __name__ == "__main__":
    main()
