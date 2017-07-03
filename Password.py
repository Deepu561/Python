#Password Generator
 
import random
s = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
passlen = 8
password = ''.join(random.sample(s,passlen))
print(password)

#Password Generator using function

import random
import string

def pw_gn(size = 8, chars = string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for x in range(size))

print(pw_gn(int(input("Enter the size of your password\n"))))
