# mortgage.py
#
# Exercise 1.7

principal = 500000.00
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month = month + 1

    if int(month) >= int(extra_payment_start_month) and int(month) <= int(extra_payment_end_month):
        extra = extra_payment
    
    else:
        extra = 0

    total_payment = payment + extra

    if total_payment > principal:
        total_paid = total_paid + principal
        principal = 0
    else:
        principal = principal * (1+rate/12) - total_payment
        total_paid = total_paid + total_payment

    out = f'Month: {month}, ${total_paid:0.2f} paid, ${principal:0.2f} remaining'
    print(out)


out = f'Paid {total_paid:0.2f} in total over {month} months.'
print(out)
