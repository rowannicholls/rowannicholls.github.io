"""Generic strong passwords."""
import secrets
import string

# - Alphanumerics (numbers and letters)
# - At least twelve characters
# - At least one lowercase character
# - At least one uppercase character
# - At least one special character
# - At least two digits
# - No run of three or more consecutive numbers
# - No run of three or more consecutive letters
alphabet = string.ascii_letters + string.digits + string.punctuation
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(12))
    if (
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c in string.punctuation for c in password) and
        sum(c.isdigit() for c in password) >= 3 and
        not any(
            all(
                [
                    password[i].isdigit(),
                    password[i + 1].isdigit(),
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

# - Alphanumerics (both numbers and letters)
# - Five characters
# - Lowercase letters
# - No "l" or "o"
alphabet = string.ascii_letters + string.digits
codes = []
while len(codes) < 10:
    while True:
        code = ''.join(secrets.choice(alphabet) for i in range(5))
        code = code.lower()
        if ('l' not in code) and ('o' not in code):
            break
    if code not in codes:
        codes.append(code)
print(codes)

# - At least twelve characters
# - At least one lowercase character
# - At least one uppercase character
# - Exactly one special character
# - At least two digits
# - No run of three or more consecutive numbers
# - No run of three or more consecutive letters
alphabet = string.ascii_letters + string.digits + '!“£%&?'
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(12))
    if (
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        sum(
            int(b) for b in [c in '!“£%&?' for c in password]
        ) == 1 and
        sum(c.isdigit() for c in password) >= 3 and
        not any(
            all(
                [
                    password[i].isdigit(),
                    password[i + 1].isdigit(),
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
