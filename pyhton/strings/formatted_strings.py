# bad
first = 'Rodrigo'
last = 'Andrade'
message = first + ' [' + last + '] is a coder'
print(message) 

# good
msg = f'{first} [{last}] is a coder'
print(msg)