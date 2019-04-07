x = 10 + 3 * 2
print(x)

## order operator precedence
# 1 - parenthesis
# 2 - exponentitation 2 ** 2
# 3 - multiplication or division
# 4 - addition or subtraction

y = 10 + 3 * 2 ** 2
print(y) # 22

z = (10 + 3) * 2
print(z) # 26

y = 10 + (3 * 2) ** 2
print(y) # 46

w = (10 + (3 * 2) ** 2) / 2
print(w) # 23