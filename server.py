from flask import Flask, render_template
app = Flask(__name__) 

# @app.route('/')
# def hello():
#     return "It works"

@app.route('/')
def renderNoPass():
    # http://localhost:5000 - should display 8 by 8 checkerboard
    # return render_template('index.html', color1='red' , color2= 'black')
    return render_template("index.html",x=8, y=8,color1='red', color2='black' ) 

@app.route('/<int:y>')
def renderPassY(y):
  # http://localhost:5000/4 - should display 8 by 4 checkerboard
   
    return render_template("index.html",x=8, y=y,color1='red', color2='black' ) 


@app.route('/<int:x>/<int:y>')
def renderXY(x, y):
 # http://localhost:5000/(x)/(y) - should display x by y checkerboard.  
    return render_template("index.html",x=x, y=y,color1='red', color2='black' ) 

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def renderAll(x, y, color1, color2):
# SENSEI BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2
    return render_template("index.html",x=x, y=y,color1=color1, color2=color2 ) 







if __name__=="__main__": 
    app.run(debug=True)