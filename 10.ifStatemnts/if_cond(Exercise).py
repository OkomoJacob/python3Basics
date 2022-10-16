price = 1000000
good_credit = True
bad_credit = False

if good_credit:
    _down_payment = 0.1 * price

elif bad_credit:
    _down_payment = 0.2 * price
print(f"Downpayment is Ksh.{_down_payment}")
