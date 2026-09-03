# convert the time entered in hh,min and sec into seconds.
hh = int(input('enter the hour:'))
mm = int(input('enter the minutes:'))
ss = int(input('enter the seconds:'))
total_seconds = (hh * 3600)+(mm *60) + ss
print('total seconds =',total_seconds)       

