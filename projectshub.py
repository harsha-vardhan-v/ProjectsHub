from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1> About </h1>'

if __name__ == '__main__':
    app.run(debug=True)
