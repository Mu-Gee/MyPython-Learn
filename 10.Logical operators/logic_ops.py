# Logical Operators
has_high_income = False
has_good_credit = True
has_criminal_record = True
# Both conditions should be true
if has_high_income and has_good_credit:
    print("Eligible for loan")
# At least one condition has to be true
if has_high_income or has_good_credit:
    print("Eligible for partial loan")
# NOT inverses any boolean value
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
