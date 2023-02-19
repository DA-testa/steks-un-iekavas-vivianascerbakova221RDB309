# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    
    
    for position, character in enumerate(text):
        if character in "([{":
            # Process opening bracket, write your code here
            
            opening_brackets_stack.append(Bracket(character, position + 1)) #bracket character = next; bracket position = position
            pass

        if character in ")]}":

            
            # Process closing bracket, write your code here
            
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, character):
                return position + 1
            opening_brackets_stack.pop()
            
    if opening_brackets_stack :
        return opening_brackets_stack[0].position
    return "Success"

        
def main():
    command = input()
    if("I" in command):
        text = input()
    elif("F" in command):
        print()
    else:
        return
                                      
    mismatch = find_mismatch(text)
                                      
    # Printing answer, write your code here
    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
