def simplify_path(path):
    stack = []
    components = path.split('/')

    for component in components:
        if component == '..':
            if stack:
                stack.pop()
        elif component and component != '.':
            stack.append(component)

    return '/' + '/'.join(stack)

input_path = "/home/../usr//bin/./test"
output_path = simplify_path(input_path)
print(output_path)