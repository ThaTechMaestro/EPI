def test_valid_parenthesis(s):


    stack = []

    length = len(s)

    for i in range(length):

        stack_len = len(stack)

        if stack_len == 0:
            stack.append(s[i])
        elif s[i] == ")" and stack[stack_len-1] == "(":
            stack.pop(stack_len - 1)
        elif s[i] == "}" and stack[stack_len-1] == "{":
            stack.pop(stack_len-1)

