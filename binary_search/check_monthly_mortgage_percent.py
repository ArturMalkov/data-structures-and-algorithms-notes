# interest is x% per year, loan term is n months and the amount of loan is m.
# what is the size of annuity monthly payment?

def f_bin_search(left, right, eps, check, check_params):
    while left + eps < right:
        middle = (left + right) / 2
        if check(middle, check_params):
            right = middle
        else:
            left = middle

    return left


def check_monthly_percent(monthly_percent, yearly_percent):
    month_sum = 1 + monthly_percent / 100
    year_sum = 1 + yearly_percent / 100
    return month_sum ** 12 >= year_sum


def check_credit(monthly_pay, params):
    periods, credit_sum, monthly_percent = params
    for i in range(periods):
        percent_pay = credit_sum * (monthly_percent / 100)
        credit_sum -= monthly_pay - percent_pay

    return credit_sum <= 0


x = 12  # yearly percent
eps = 0.0001
monthly_percent = f_bin_search(0, x, eps, check_monthly_percent, x)

eps = 0.01
m = 10_000_000
n = 300
monthly_pay = f_bin_search(0, m, eps, check_credit, (n, m, monthly_percent))
