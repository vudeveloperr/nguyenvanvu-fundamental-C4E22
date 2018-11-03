from mongoengine import Document , StringField , DictField ,IntField
# mo ta du lieu
class Regis(Document):
    First_Name = StringField()
    Last_Name = StringField()
    Email = StringField()
    YOB = IntField()
    Gender = StringField()
    City = StringField()