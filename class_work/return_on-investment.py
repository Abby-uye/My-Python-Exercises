
amount_invested = float(input("Enter the amount you want to invest: "))


for deposit in range(1, 31):
    roi = amount_invested * 0.10
    new_amount = amount_invested + roi
    amount_invested = new_amount

    print(f"Your Roi is {roi:.2f} and your investment is now {amount_invested:.2f} in year {deposit}")



