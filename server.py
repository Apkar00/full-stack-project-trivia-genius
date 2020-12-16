<<<<<<< HEAD
from flask import Flask, Response, request,render_template


app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/sign_up", methods=['POST'])
def add_user():
    name = request.form.get("UserName")
    password=request.form.get("psw")
    print(name,password)
    return render_template('home.html')#change to profile page

@app.route("/log-in", methods=['POST'])
def check_user():
    name = request.form.get("UserName")
    password=request.form.get("psw")
    print(name,password)
    return render_template('home.html')#change to profile page

if __name__ == '__main__':
    app.run(port=3001)
=======
from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')


@app.route('/')
def root():
    return render_template('home.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/profile/<username>')
def profile(username):
    return render_template('home2.html', item={'username': username})


if __name__ == '__main__':
    app.run(port=3000)
>>>>>>> main
