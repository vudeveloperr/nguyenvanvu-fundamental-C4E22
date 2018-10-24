from flask import Flask
app = Flask(__name__)

@app.route("/user/<username>")
def users(username):
    users = {
	"huy" : {
		"name" : "nguyen quang huy",
		"age" : 29,
        "gender" : "male",
        "hobby" : "eat"
       },
    "tuananh" : {
			"name" : "Huynh Tuan Anh",
			"age" : 22,
            "gender" : " male",
            "hobby" : " ...."
       },
    "quan" : {
        "name" : "quan",
        "age" : "21",
        "gender" : "male",
        "hobby" : "coding"
    },  
    }
    return str(users)

if __name__ == '__main__':
  app.run(debug=True)