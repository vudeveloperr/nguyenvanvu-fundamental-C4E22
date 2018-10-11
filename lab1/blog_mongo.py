from pymongo import MongoClient

uri = "mongodb://vanvuadmin:c4e22vanvu@ds111066.mlab.com:11066/c4e22"

#connect to database
client = MongoClient(uri)
db = client.get_default_database()


#collection
posts = db['posts'] #insert_one(C), find (R)

post_list = posts.find()
for p in post_list:
    
    print(p['author'])
    print(p['title'])
    print(p['content'])

#document
#create a document
# post = {
#     'title' : 'hom nay troi am u ',
#     'content':'toi van o nha',
#     'author':'me'
# }
# #insert created (document
# posts.insert_one(post)

