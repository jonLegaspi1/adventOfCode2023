# Problem prompt can be found at: https://adventofcode.com/2023/day/1
# Problem can be solved using a stack to retrieve the 
# first and last digit in a string
# Process is as follows:
# 1. For each char in string s, check if char from string is digit
# 2. If not digit, skip
# 3. If digit, push onto stack
# 4. Last digit is top of the stack
# 5. If stack is empty, first digit = last digit
# 6. If stack is not empty, first digit = first element of stack
# 7. Return first + last digit
# 8. Keep a running sum of each string in input file

def retDigit(s: str) -> int:
    # init stack, first, and last variables
    stack = []
    first, last = 0, 0
    # for each character in string s
    for char in s:
        if char.isdigit():
            # if character is digit, push onto stack
            stack.append(char)
    last = stack[-1]
    if not stack:
        first = last
    first = stack[0]
    return int(str(first) + str(last))
#open input file, line by line
f = open("day1_input.txt", "r")
sum = 0
#for each line in file f
for line in f:
    sum += retDigit(line)
print("Sum: ", sum)