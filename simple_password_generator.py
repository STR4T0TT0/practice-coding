# Never use the random module 
import string
import secrets

# punctuation will provide !”#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
PasswordComplexity = string.ascii_letters + string.digits + string.punctuation
PasswordLength = 15
PasswordMinimumNumbers = 2

while True:
    GeneratedPassword = ''.join(secrets.choice(PasswordComplexity) for i in range(PasswordLength))
    if (any(c.islower() for c in GeneratedPassword)
            and any(c.isupper() for c in GeneratedPassword)
            and sum(c.isdigit() for c in GeneratedPassword) >= PasswordMinimumNumbers):
        break

print('You can use ',GeneratedPassword)
del GeneratedPassword, PasswordComplexity