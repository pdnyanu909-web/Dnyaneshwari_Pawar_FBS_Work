#WAP to input any alphabet and check whether it is vowel or consonant

ch = str(input('enter any alpha:'))
if ch.lower()in['a','e','i','o','u']:
    print('vowel')
else:
    print('consonant')
