def isValid(s):
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets.keys():
                if not stack or brackets[char] != stack.pop():
                    return False
            else:
                continue
        return not stack
    
input_string = "{[()]}"

if isValid(input_string):
    print("True")
else:
    print("False")