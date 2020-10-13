"""
Generic strong passwords.

Often when websites require a strong password they want something that contains:

- Alphanumerics (numbers and letters)
- At least 10 characters
- At least one lowercase character
- At least one uppercase character
- At least one special character
- At least one digit
- No three or more consecutive numbers
- No three or more consecutive letters

Here's a snippet that will do that:
"""
import secrets
import string

alphabet = string.ascii_letters + string.digits + string.punctuation
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(12))
    if (
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c in string.punctuation for c in password) and
        any(c.isdigit() for c in password) and
        not any(all([password[i].isdigit(), password[i + 1].isdigit(), password[i + 2].isdigit()]) for i, c in enumerate(password[:-2])) and
        not any(all([password[i] in string.ascii_letters, password[i + 1] in string.ascii_letters, password[i + 2] in string.ascii_letters]) for i, c in enumerate(password[:-2]))
    ):
        break
print(password)
