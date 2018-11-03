from poll import Poll
import string
import mlab
from random import choice

#1 . Connect to database
mlab.connect()


#2. prepare data
q = "hackathon an gi ?"
opts = [
    "an pizza ",
    " hoi an bread",
    "pho xao"
]

alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
c = ""
for _ in range(6):
    c+= choice(alphabet)
print(c)
#3.create data
p = Poll(question=q , options=opts,code =c)


#4.save
p.save()
