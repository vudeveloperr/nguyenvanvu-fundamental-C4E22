from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#connect to database

client = MongoClient(uri)
db = client.get_default_database()

# collection
posts = db['posts']

#document
# create document
# post = {
#     'author' : "nguyễn trọng tài ",
#     'title':'HongKong1',
#     'content' : """Và giờ anh biết chuyện tình mình chẳng còn gì 
#                     Khi nắng xuân sang lời mật ngọt còn thầm thì 
#                     Em bước sang ngang đợi chờ một điều diệu kì 
#                     Như lúc ban đầu 
#                     Và giờ em khóc thì cũng chẳng để làm gì 
#                     Đâu phải cho anh chuyện tình mình mà là vì 
#                     Em đã trao ai, dòng lệ tràn đầy cầu kì 
#                     Những năm tháng phai nhòa """,
#     'by':'vanvu'                

# }
# post = {
#     'title':'Buồn',
#     'author':'me',
#     'content':"""
#     Buồn là một trong những tâm trạng cảm xúc của con người 
#     mọi cảm xúc có thể bị mất , khiến trạng thái tinh thần luôn 
#     biếm động theo dòng suy nghĩ miên man
#     ví dụ : BUỒN CƯỜI! 
#     """
# }

# post = {
#     'title':'Nói chung là...',
#     'author':'xoay',
#     'content':'''
#     Trời nắng! Nói chung là vui 
#     Ta đi lang thang nhìn ngắm cuộc đời . 
#     Trời mưa! Nói chung cũng vui. 
#     Anh em bên nhau hàn huyên chờ trời nắng. 
#     Đi làm! Nói chung cũng vui. Bao nhiêu đam mê cống hiến choi đời. 
#     Đi chơi! Đương nhiên là vui. Hôm nay đi chơi rồi mai đi làm. 
#     Vắng em, nói chung là buồn. 
#     Xa em, nói chung cũng buồn. 
#     Cuộc đời nói chung là vui, chỉ mỗi vắng em nói chung là buồn.
#     '''
# }
post = {
    'title':'cảm nhận',
    'author':'me',
    'content':'''lớp vui các anh chị hay support hay giúp đỡ 
    hết ồi hihi
    '''
}


# Insert create document 
posts.insert_one(post)