import datetime
#age = int(input('please enter your date of birth'))

day = int(input('Day: '))

mnt = int(input('Month: '))

yr = int(input('year: '))

dateOfBirth = datetime.datetime(yr, mnt, day)
print ('Converted date is:', dateOfBirth)

#Tday = int(input('Current Date: '))

#Tmnt = int(input('Current Month: '))

#Tyr = int(input('Current Year: '))

currenttime = datetime.datetime.now()


# q = Tyr-yr
# w = Tmnt-mnt 
# e = Tday-day
# print('You are',q,'years', w,'months', e, 'days old.')

# calc difference of time
duration = dateOfBirth - currenttime
print (duration)
