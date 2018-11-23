from flask import Flask,render_template, request ,redirect, url_for
from random import choice


from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/payment")
def payment():
  return render_template("payment.html")  

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/signup") 
def signup():
  return render_template("signup.html") 

@app.route("/nhadautu")
def nhadautu():
  return render_template("nhadautu.html") 

@app.route("/startup") 
def startup():
  return render_template("startup.html") 

@app.route("/company_profile")
def company_profile():
  return render_template("company_profile.html")


if __name__ == '__main__':
  app.run(debug=True)