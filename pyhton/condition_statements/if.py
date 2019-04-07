import math

is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold: 
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print('Enjoy your day')


###
good_credit = False
price_house = 1000000
put_down = .2

if good_credit:
    put_down = .1
    print('You need to put down 10%')
else:
    print('you need to put down 20%')
print(f'Down payment is: ${math.floor(price_house * put_down)}')