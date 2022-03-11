from datetime import date
 
def calculateAge(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) <(birthdate.month, birthdate.day))
    return age
     
# Driver code
year = int(input('Enter your birth year: '))
month = int(input('Enter your birth month: '))
day = int(input('Enter your birth date: '))
birthdate = date(year, month, day)

print("You are ", calculateAge(birthdate), "years old")