from hashlib import md5
from operator import eq

a = 2000036716066
while True:
    a = a + 1
    print(a)
    if eq("5F0011B9DF6A8D220F46CBADA15F9F92", str(md5(str(a).encode()).hexdigest().upper())):
        break
