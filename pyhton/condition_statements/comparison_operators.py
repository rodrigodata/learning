temperature = 20

# greater or equal then
if temperature >= 30:
    print("It's a hot day")
# lesser or equal then 
elif temperature <= 10:
    print("It's a cold day")
else:
    print("The weather is lovely")

# equal
age = 28

if age == 27:
    print('You are 27 years old')
elif age == 28:
    print('You are 28 years old')
else:
    print('...')

# not equal
name = input('Please, tell me your name: ')

if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('Name looks good :)')
    