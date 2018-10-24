from flask import Flask,render_template
app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bodymassindex(weight,height):
    bmi = (weight)/((height*0.01)*(height*0.01))
    if bmi<16:
        return "weight loss"
    elif 16<=bmi<18.5 :
        return "Lack of weight"
    elif 18.5<=bmi<25 :
        return "normally"
    elif 25<=bmi<=30 :
        return "Overweight"
    else :
        return "Obesity"     
              

if __name__ == '__main__':
  app.run(debug=True)