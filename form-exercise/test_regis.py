from regis import Regis
from random import choice
import string
import mlab

#1. Connect to database
mlab.connect()

#2.prepare data
F = ""
L = ""
E = ""
Y = ""
G = ""
C = "" 

#3. create data 
r = Regis(First_Name=F,Last_Name=L,Email=E,YOB=Y,Gender=G,City=C)


#4.save
p.save()