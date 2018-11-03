from flask import Flask,render_template, request
import mlab
from regis import Regis


app = Flask(__name__)
mlab.connect()
@app.route("/form_exercise", methods=['GET','POST'])
def form_exercise():
  if request.method == "GET":  
    return render_template("register.html")
  elif request.method == "POST":  
    # unpack data(form) 
    form = request.form
    First_Name = form["First_Name"]
    print(First_Name)
    Last_Name = form['Last_Name']
    print(Last_Name)
    Email = form['Email']
    print(Email)
    YOB = form['YOB']
    print(YOB)
    Gender = form['Gender']
    print(Gender)
    City = form['City']
    print(City)
    r = Regis(First_Name=First_Name,Last_Name=Last_Name,Email=Email,YOB=YOB,Gender=Gender,City=City)
    r.save()
    return "ok"
if __name__ == '__main__':
  app.run(debug=True)