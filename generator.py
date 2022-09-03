#just interested because of youtube

import secrets
import string

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))

print("Here's Your Password :")
print(password)