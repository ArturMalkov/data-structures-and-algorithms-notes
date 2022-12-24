# 233 -> binary
# 233 // 2 = 116; rem = 1
# 116 // 2 = 58; rem = 0
# 58 // 2 = 29; rem = 0
# 29 // 2 = 14; rem = 1
# 14 // 2 = 7; rem = 0
# 7 // 2 = 3; rem = 1
# 3 // 2 = 1; rem = 1;
# 1 // 2 = 0; rem = 1

def find_binary(decimal, result=""):
    if decimal == 0:
        return result
    result = str(decimal % 2) + result
    return find_binary(decimal // 2, result)


print(find_binary(233))
