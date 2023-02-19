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

            
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[len(opening_brackets_stack)-1][0], next):
                return position + 1
                
            if are_matching(opening_brackets_stack[len(opening_brackets_stack)-1][0], next):
                opening_brackets_stack.pop()
            pass
     # Process closing bracket, write your code here
        
    if opening_brackets_stack :
        return opening_brackets_stack[len(opening_brackets_stack)-1[1] + 1


def main():
    input = input()
    if('I' in input):
        text = input()
    elif('F' in input):
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
