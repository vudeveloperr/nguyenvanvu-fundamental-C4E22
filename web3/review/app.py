from flask import Flask , render_template , request
app = Flask(__name__)

@app.route("/asurvey", methods=['GET','POST'])
def asurvey():
  if request.method == "GET":  
    return render_template("review.html")
  elif request.method == "POST":
    # unpack data(form) 
    form = request.form
    # asurvey = form['asurvey']
    options = []
    for k,v in form.items():
        options.append(v)
    print(options)
    return "gotcha"
if __name__ == '__main__':
  app.run(debug=True)