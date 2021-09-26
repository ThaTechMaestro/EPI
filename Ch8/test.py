# https://leetcode.com/problems/valid-parentheses/discuss/1407199/EASY-SOLUTION-or-PYTHON-or-FATER-THAN-90-or-please-upvote
# Checking a new solution
# I will continue from here tommorow morning

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

