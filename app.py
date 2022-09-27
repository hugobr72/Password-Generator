import random

lowerCase = 'abcdefghijklmnopqrstuvwxyz'
upperCase = lowerCase.upper()
number = '1234567890'
specialCharacters = '!@#$%^&*()|\/'

passLett = lowerCase + upperCase + number + specialCharacters
passCount = 10

password = "".join(random.sample(passLett, passCount))
print(password)