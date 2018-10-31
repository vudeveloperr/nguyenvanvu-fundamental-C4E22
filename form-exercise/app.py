from flask import Flask,render_template, request
app = Flask(__name__)

@app.route("/form_exercise", methods=['GET','POST'])
def form_exercise():
  if request.method == "GET":  
    return render_template("register.html")
  elif request.method == "POST":  
    # unpack data(form) 
    form = request.form
    return str(form)
    
    
    

    # Last_Name = form['Last Name']
    # return Last_Name

    # Email = form['Email']
    # return Email

    # YOB = form['YOB']
    # return YOB

    # Gender = form['Gender']
    # return Gender

    # City = form['City']
    # return City

    
if __name__ == '__main__':
  app.run(debug=True)