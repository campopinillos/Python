#!/usr/bin/env python3
# phone and email detector sample in https://www.blackbaud.com/files/customreports/PhoneDirectory_web.pdf
import re
import pyperclip

# This get whatever you have in control + C and paste to a variable
message = pyperclip.paste()

phoneRegex = re.compile(r'''(
((\d\d\d)|(\(\d\d\d\)))?	# area code
(\s|-)						# separator
\d{3}						# first 3 digits
-							# separator
\d{4}						# last 4 digits
(((ext(\.)?\s)|x)			# extension
(\d{2,5}))?					#num extension
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+	# username
@					# @ symbol
[a-zA-Z0-9._%+-]+	# domain name
# (\.[a-zA-Z]{2,4})	# dot-something
)''', re.VERBOSE)


extractedPhone = phoneRegex.findall(message)
extractedEmail = emailRegex.findall(message)

allPhoneNumbers = []
for phoneNum in extractedPhone:
    allPhoneNumbers.append(phoneNum[0])

print(allPhoneNumbers)
print(extractedEmail)
result = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
# This get whatever resul you have and get in control + C to paste to other place
pyperclip.copy(result)
