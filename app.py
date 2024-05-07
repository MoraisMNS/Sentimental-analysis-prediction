from flask import Flask, render_template,request

app = Flask(__name__)

data = dict()

reviews = ['Good product', 'Bad product','I like it']
positive = 2
negative = 1

@app.route("/")
def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative
    return render_template('index.html', data=data)

@app.route("/",methods = ['post'])

def my_post():
    text = request.form['text']


if __name__ == "__main__":
    app.run()