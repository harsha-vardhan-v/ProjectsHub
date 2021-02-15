from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/login')
def home():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
