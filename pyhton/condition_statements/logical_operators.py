has_high_income = True
has_good_credit = True
criminal_record = True

# and
if has_high_income and has_good_credit:
    print('Eligible for loan. High income & Good credit')

# or
if has_good_credit or has_high_income:
    print('Eligible for loan. High income or Good credit')

# not
if has_good_credit and not criminal_record:
    print('Eligible for loan. Good credit & not criminal record')