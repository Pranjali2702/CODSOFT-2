import random
import string
length=int(input('enter the length of the required password'))
for i in range(length):
    password=random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation ,k=length)
    res=''.join(password)
print(res)