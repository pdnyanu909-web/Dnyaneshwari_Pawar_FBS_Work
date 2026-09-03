#convert day into years, weeks and day
#  take input
Day = int(input('enter number of days:'))
# calculate years 
years = Day // 365

#calculate remaining days
Remainingday = Day % 365
#calculate  weeks
weeks = Remainingday // 7 
#calculate days
Days = Remainingday % 7
# display result
print('years:', years)
print('weeks:',weeks)
print('days:',Day)