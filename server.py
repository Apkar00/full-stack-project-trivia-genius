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
