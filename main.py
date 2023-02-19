# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    
    
    for position, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            
            opening_brackets_stack.append(Bracket(next, position)) #bracket character = next; bracket position = position
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            
            if not opening_brackets_stack[len(opening_brackets_stack)-1][0], next):
                opening_brackets_stack.pop()
            pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
