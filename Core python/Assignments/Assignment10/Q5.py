# Accept a number from user and check if this element is present in the list or not.
#  Also tell how many times it is present in the list.

a = [10,20,10,30,10,40]
num = int(input('enter num:'))
count = 0
for i in a:
    if i == num:
        count = count + 1
if count > 0:
           print('element is present')            
           print('element is present',count,'times')
else:
      print('element is not present')

