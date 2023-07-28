## create a simple flask application
from flask import Flask, render_template # Also import redirect, url_for or render_template
## Create flask app

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello World"
#   return "<p>Hello, World!</p>" these are para (paragraph)tags <P>
#   return "<h1>Hello, world</h1>" these are html or h1 tags <h>
# we can learn more tags from html tutorials (it basecally change the fonts)

@app.route('/welcome')
def welcome():
    return "Wlecome to the flask tutorials"

@app.route('/index')
def index():
    #return "Welcome to the index"
    return render_template('index.html')



if __name__ =='__main__':
    app.run()
    #app.run(debug=True)   here we use in development phase,
    #we debug our code and get the issues. it done update sidebyside
