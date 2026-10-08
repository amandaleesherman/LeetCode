def valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values(): #opening brackets 
            stack.append(char)
        elif char in mapping.keys(): #closing brackets
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack