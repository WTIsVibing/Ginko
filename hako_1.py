rates = [0.3575, 0.3756, 0.4950]

taxable_income_limit_1 = 38883 
taxable_income_limit_2 = 78426
taxable_income_limit_delta = taxable_income_limit_2 - taxable_income_limit_1

taxable_income_ranges = [38883, taxable_income_limit_delta, 0]

def calc_tax(income, age):
    income_tax = 0

    if age < 67:
        for i,rate in enumerate(rates):
            if income < 0:
                break
            income_tax = income_tax + income * rate
            income = income - taxable_income_ranges[i]
    else:
        print("You should be pensioned")
        income_tax = 0
    return round(income_tax,2)
