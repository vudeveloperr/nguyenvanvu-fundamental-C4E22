from mongoengine import Document , StringField , ListField
# mo ta du lieu
class Poll(Document):
    question = StringField()
    options = ListField(StringField())
    code = StringField()
