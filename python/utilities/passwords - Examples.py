"""Generic strong passwords."""
import secrets
import string

# Often when websites require a strong password they want something that
# contains:
#
# - Alphanumerics (numbers and letters)
# - At least 12 characters
# - At least one lowercase character
# - At least one uppercase character
# - At least one special character
# - At least one digit
# - No three or more consecutive numbers
# - No three or more consecutive letters
#
# Here's a snippet that will do that:
alphabet = string.ascii_letters + string.digits + string.punctuation
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(12))
    if (
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c in string.punctuation for c in password) and
        any(c.isdigit() for c in password) and
        not any(
            all(
                [
                    password[i].isdigit(), password[i + 1].isdigit(),
                    password[i + 2].isdigit()
                ]
            ) for i, c in enumerate(password[:-2])
        ) and
        not any(
            all(
                [
                    password[i] in string.ascii_letters,
                    password[i + 1] in string.ascii_letters,
                    password[i + 2] in string.ascii_letters
                ]
            ) for i, c in enumerate(password[:-2])
        )
    ):
        break
print(password)

# - Alphanumerics (numbers and letters)
# - At least 12 characters
# - At least one lowercase character
# - At least one uppercase character
# - At least one digit
# - No three or more consecutive numbers
# - No three or more consecutive letters
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(12))
    if (
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        not any(
            all(
                [
                    password[i].isdigit(), password[i + 1].isdigit(),
                    password[i + 2].isdigit()
                ]
            ) for i, c in enumerate(password[:-2])
        ) and
        not any(
            all(
                [
                    password[i] in string.ascii_letters,
                    password[i + 1] in string.ascii_letters,
                    password[i + 2] in string.ascii_letters
                ]
            ) for i, c in enumerate(password[:-2])
        )
    ):
        break
print(password)

# - Alphanumerics (numbers and letters)
# - At least ten characters
# - At least one lowercase character
# - At least one uppercase character
# - At least one special character
# - At least two digits
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
# print(password)

# - Alphanumerics (numbers and letters)
# - At least 14 characters
# - At least one lowercase character
# - At least one uppercase character
# - At least one digit
# - No three or more consecutive numbers
# - No three or more consecutive letters
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(14))
    if (
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        not any(
            all(
                [
                    password[i].isdigit(), password[i + 1].isdigit(),
                    password[i + 2].isdigit()
                ]
            ) for i, c in enumerate(password[:-2])
        ) and
        not any(
            all(
                [
                    password[i] in string.ascii_letters,
                    password[i + 1] in string.ascii_letters,
                    password[i + 2] in string.ascii_letters
                ]
            ) for i, c in enumerate(password[:-2])
        )
    ):
        break
# print(password)

# XKCD-style passwords
with open('/usr/share/dict/words') as f:
    words = [word.strip() for word in f]
    password = ' '.join(secrets.choice(words) for i in range(4))
# print(password)
