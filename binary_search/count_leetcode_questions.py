# when preparing for an interview, you chose n leetcode questions.
# on the first day, you solved k questions, and each next day you solve 1 leetcode question more than the day before.
# how many days will it take you to prepare for an interview?
from turtle import left


def left_binary_search(left, right, check, check_params):
    while left < right:  # left is the minimum number of days needed - initially equals 0
        middle = (left + right) // 2  # right is the maximum number of days needed - initially equals to n - number of leetcode questions chosen - you will definitely solve n questions in n days
        if check(middle, check_params):
            right = middle
        else:
            left = middle + 1

    return left


def check_leetcode_questions_count(days, params):
    n, k = params  # n is the total number of leetcode questions, k - number of leetcode questions solved on the first day
    return (k + (k + days - 1)) * days // 2 >= n


num_of_leetcode_questions = 180
num_of_days_to_prepare = left_binary_search(0, num_of_leetcode_questions, check_leetcode_questions_count, (num_of_leetcode_questions, 1))
print(num_of_days_to_prepare)
