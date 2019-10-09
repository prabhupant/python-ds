from re import sub, compile 

'''
    \w unicode characters [a-zA-z0-9]
    \s white spaces       [\b\n\r\f\v]
    ^ invert the pattern
'''

pattern = compile(r'[^\w|\s]')

s = 'Hi! This is an example, this text contains a lot of characters and numbers (1,2,3,4).'

out = sub(pattern, ' ', s)
print(s)
print(out)
