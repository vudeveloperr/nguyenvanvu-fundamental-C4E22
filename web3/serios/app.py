from flask import Flask , render_template ,request
app = Flask(__name__)

@app.route("/new_bike" , methods= ["GET", "POST"])
def new_bike():
  if request.method == "GET":
    return render_template("new_bike.html")

  elif request.method == "POST":
    form = request.form
    
    options = []
    for k,v in form.items():
        options.append(v)
    print(options)
    return "gotcha"

if __name__ == '__main__':
  app.run(debug=True)