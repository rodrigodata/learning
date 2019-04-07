# get data from inputs
# normalize data from input
# convert
import math

user_weight = input('Weight: ')
type_user_weight = input('(L)bs or (K)g: ')
lbs_kg = 0.45359237
user_weight_converted = 0

# normalize weight
user_weight = int(user_weight)
# normalize type user weight
type_user_weight = str(type_user_weight).upper()
# find type to convert
if type_user_weight == 'L':
    user_weight_converted = user_weight * lbs_kg
    print(f'You weight ~{math.ceil(user_weight_converted)} kg')
elif type_user_weight == 'K':
    user_weight_converted = user_weight / lbs_kg
    print(f'You weight ~{math.ceil(user_weight_converted)} lbs')
else:
    print('Type of measure not found. Please enter L or K.')
