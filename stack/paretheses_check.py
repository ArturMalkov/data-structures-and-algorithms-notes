a = input("Please enter a string: ")
stack = []
verify_flag = True

for lt in a:
    if lt in "({[":
        stack.append(lt)
    elif lt in ")}]":
        if len(stack) == 0:  # closing parentheses > opening parentheses
            verify_flag = False
            break

        br = stack.pop()
        if br == "(" and lt == ")":
            continue
        if br == "[" and lt == "]":
            continue
        if br == "{" and lt == "}":
            continue

        verify_flag = False  # if checks above failed
        break

if verify_flag and len(stack) == 0:  # after all the checks, stack must be empty
    print("Yes")
else:  # opening parentheses > closing parentheses
    print("No")
