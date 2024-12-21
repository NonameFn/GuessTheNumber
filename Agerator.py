import datetime

# Get the user's date of birth
day = int(input('Day of birth: '))
month = int(input('Month of birth: '))
year = int(input('Year of birth: '))

# Convert the date of birth to a datetime object
date_of_birth = datetime.datetime(year, month, day)

# Get the current date
current_date = datetime.datetime.now()

# Calculate the difference in days
age_in_days = (current_date - date_of_birth).days

# Print the result
print(f'You have been alive for {age_in_days} days.')