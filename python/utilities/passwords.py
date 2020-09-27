"""
Generic strong passwords.

Often when websites require strong passwords they want something that contains:

- Alphanumerics (numbers and letters)
- At least ten characters
- At least one lowercase character
- At least one uppercase character
- At least one special character
- At least two digits

Here's a snippet that will do that:
"""
import secrets
import string

alphabet = string.ascii_letters + string.digits + string.punctuation
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    if (
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c in string.punctuation for c in password) and
        sum(c.isdigit() for c in password) >= 3
    ):
        break
print(password)
