# len() => Python function
myStr = 'Minha string'
print(len(myStr))

# methods
# upper
print(myStr.upper())
# lower
print(myStr.lower())
# find => retorna o index
print(myStr.find('t'))
print(myStr.find('M'))
print(myStr.find('string'))
print(myStr.find('O'))
# replace
print(myStr.replace('string', 'STRING')) # works
print(myStr.replace('String', 'STRING')) # do not works
# in
print('string' in myStr) # true
print('String' in myStr) # false