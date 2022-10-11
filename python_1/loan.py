loan_amt = float(input("How large is the loan? "))
credit_score = float(input("How good is your credit history? "))
income = float(input("How high is your income? "))
down_pay = float(input("How large is your down payment? "))
approved = False

if loan_amt >= 5:
    if credit_score >= 7 and loan_amt >= 7:
        approved = True
    elif credit_score >= 7 or income >= 7:
        if down_pay >= 5:
            approved = True
        else:
            approved = False
else:
    if credit_score < 4:
        approved = False
    elif income >= 7 or down_pay >= 7:
        approved = True
    elif income >= 4 and down_pay >= 4:
        approved = True
    else:
        approved = False

if approved == True:
    print("You are approved for a loan!")
else:
    print("You are not approved for a loan....")