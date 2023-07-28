from flask import Flask, render_template

score=Flask(__name__)

@score.route('/')
def home():
    return "Hello Candidate"

@score.route('/success/<int:score>')
def success(score):
    return "the person has passed and the score is "+ str(score)




if __name__ == '__main__':
    score.run(debug=True)