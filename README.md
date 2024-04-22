# Custom Language Interpreter

This Python script acts as a simple interpreter for a custom scripting language, designed to manipulate strings and numbers using a stack-based approach. The script reads instructions from a text file and executes a series of commands based on those instructions.
Features

    REVERSE: Reverses the last string on the stack.
    REPEAT: Repeats the last string a specified number of times.
    MULTIPLY: Multiplies the last two numbers on the stack.
    PRINT: Prints a specified message.
    SPEAK: Concatenates and prints all strings on the stack until an empty string marker is encountered.
    ACCEPT: Prompts the user for input and pushes the input onto the stack.
    BREAK: Terminates the program.

# Requirements

    Python 3.x

# Setup

No additional libraries or packages are required. The script uses standard Python libraries.
Usage

    Create a text file named reverse.txt in your directory, containing the custom instructions. Each instruction should be on a new line. Here is an example of what the contents might look like:

    

PRINT Hello, this is a test.
ACCEPT
PRINT You entered:
REVERSE
PRINT Reversed input:
SPEAK

PRINT Enter two single-digit numbers to multiply:
ACCEPT
MULTIPLY
PRINT The multiplication result is:
SPEAK

PRINT Enter a character(s) to repeat:
ACCEPT
PRINT Enter the number of times to repeat the character:
ACCEPT
REPEAT
PRINT Repeated character:
SPEAK

BREAK

# Run the script from your terminal by navigating to the directory where the script is stored and using the following command:

    python interpreter.py

    Follow any prompts on the terminal to input data as required by the ACCEPT command.

# Error Handling

The script includes basic error handling for file reading issues and stack underflow conditions. Errors will cause the script to exit and display a message indicating the nature of the error and the line number on which it occurred.
Customization

You can modify the path to the instruction file or add new commands by editing the main function and adding new cases in the conditional statement handling the instructions.
