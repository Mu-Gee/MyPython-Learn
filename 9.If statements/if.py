# If Statements
is_cold = True
is_hot = True
# Executes if is_cold is true
if is_cold:
    print("It's a cold day")
    print("Dress warm")
# Executes if only is_hot is true
elif is_hot:
    print("It's a hot day")
    print("Drink water")
# Executes if both is_hot & is_cold are false
else:
    print("It's a lovely day")
print("Enjoy your day")

# House price is $1M.
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")
