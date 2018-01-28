from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
#@app.route("/")
#def index():
#    return "Flask App!"
 
#@app.route("/hello/<string:name>/")
#def hello(name):
#    return render_template(
#        'test.html',name=name)

@app.route("/")
def index():
    return render_template('test.html')

@app.route("/result", methods=['GET','POST'])
def result():
	meal = request.form['meal']
	return render_template('second.html', meal=meal)    
 
if __name__ == "__main__":
	app.run()