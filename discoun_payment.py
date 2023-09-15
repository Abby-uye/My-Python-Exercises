name =str(input("Enter name of product: "))
price = int(input("Enter price of product: "))
credit_score =bool(input("if your credit score is above 600 press True if not press ignore: "))
down_payment = 0
discount =0
if credit_score :
    down_payment = price/100*10
    discount = price/100*10
    print(f"""
    *************************
            Invoice
    *************************
    "Name of item:"  {name}  
    "Discount:    "  {discount}
    "Deposit:     "  {down_payment}
    *********************************        
    """)

else:
    down_payment = price/100*25
    print(f"""
        *************************
                Invoice
        *************************
            "Name of item:"  {name}  
            "Deposit:     "  {down_payment}
        *********************************
                                              """)







