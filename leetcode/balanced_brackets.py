
def are_brackets_valid(s: str) -> bool:

    bracket_lookup = {"}":"{", ")":"(", "]":"["}
    bracket_stack = []
    
    for char in s:
        if char in "{([":
            bracket_stack.append(char)
        else:
            if len(bracket_stack) == 0 or bracket_lookup[char] != bracket_stack[-1]:
                return False
            elif bracket_lookup[char] == bracket_stack[-1]:
                bracket_stack.pop()

    return len(bracket_stack) == 0
                


assert are_brackets_valid("()") == True
assert are_brackets_valid("()[]{}") == True
assert are_brackets_valid("(]") == False
assert are_brackets_valid("([)]") == False
assert are_brackets_valid("{[]}") == True
