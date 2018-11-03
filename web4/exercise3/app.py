from flask import Flask , render_template 
app = Flask(__name__)
import mlab
from river import River


mlab.connect()
@app.route("/river/<continent_river>")
def river(continent_river):
  #1. get poll
    name = River.objects(continent=continent_river)
    name = River.objects(length__lte =1000)
  #2.render
    return render_template("river.html", river = name)

if __name__ == '__main__':
  app.run(debug=True)