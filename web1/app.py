from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")# neu nguoi dung truy cap vao trang chu nay
def homepage():
    return " wellcome to C4e web module enjoy"

@app.route("/Quan")
def hello_quan():
    return "hello quan"  

@app.route("/praise/linh")
def praise_linh():
    return "awsome"

@app.route("/praise/<name>")
def praise(name):
    return name + " is awsome"

@app.route("/add/<int:x>/<int:y>")
def add(x,y):  # str
    s = x + y  # converte
    return str(s)

@app.route("/question")
def show_question():
    return render_template("question.html")


if __name__ == "__main__":
    app.run(debug = True)