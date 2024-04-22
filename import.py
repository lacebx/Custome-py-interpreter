import sys

def read_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read().splitlines()
    except Exception as e:
        print("Error while opening file:")
        print(e)
        sys.exit(1)

def err(msg):
    print(f"\n{msg} at line {pc}")
    sys.exit(1)

def input_text():
    return input("Write something here: ")

stack = []
pc = 0

def main():
    global pc
    lines = read_lines_from_file("/home/lace/Desktop/reverse.txt")
    stack = []

    while pc >= 0 and pc < len(lines):
        parts = lines[pc].split(" ")
        instr = parts[0]

        if instr == "REVERSE":
            if not stack:
                err("Error: Nothing to reverse")
            input_string = stack.pop()
            reversed_string = input_string[::-1]
            stack.append(reversed_string)

        elif instr == "REPEAT":
            if len(stack) < 2:
                err("Error: Not enough arguments for REPEAT")
            repeat_count = int(stack.pop())
            character = stack.pop()
            stack.append(character * repeat_count)

        elif instr == "MULTIPLY":
            if len(stack) < 2:
                err("Error: Not enough operands for multiplication")
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            result = num1 * num2
            stack.append(str(result))

        elif instr == "PRINT":
            if len(parts) < 2:
                err("Error: PRINT instruction requires an argument")
            print(" ".join(parts[1:]))

        elif instr == "SPEAK":
            stringBuilder = []
            while stack and stack[-1] != "":
                stringBuilder.insert(0, stack.pop())
            print("".join(stringBuilder))

        elif instr == "ACCEPT":
            stack.append(input_text())

        elif instr == "BREAK":
            print()
            sys.exit(0)

        else:
            # Assume any other instruction pushes its argument onto the stack
            if len(parts) > 1:
                stack.append(parts[1])

        pc += 1

if __name__ == "__main__":
    main()
