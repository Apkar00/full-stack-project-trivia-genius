
from flask import Flask, Response, request,render_template
import database_funcs
from flask import Flask, render_template, request, redirect
import database_funcs as df
from trivia.triv_api import get_question, CORRECT_ANSWERS

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

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
        result=database_funcs.check_user_name(name)
        if not result:
            database_funcs.add_user(name,password)
            return render_template('home2.html', item={'username': name})
        else:
            return render_template('sign_up.html')

@app.route("/log-in", methods=['POST'])
def check_user():
    name = request.form.get("UserName")
    password=request.form.get("psw")
    result=database_funcs.check_user(name,password)
    if result:
        return render_template('home2.html', item={'username': name})
    else:
        return render_template('log-in.html')

@app.route('/profile/<username>/quiz/<category>')
def quiz(username, category):
    user_id = df.get_user_id(username)
    print(user_id)
    print(category)
    result = get_question(id=user_id, category=category, type='multiple')
    print(result)
    print(CORRECT_ANSWERS)
    return render_template('quiz.html', item=result, username=username)


@app.route('/profile/<username>/quiz/checkAnswers', methods=['POST'])
def check(username):
    user_id = df.get_user_id(username)
    answers = request.form
    correct_answers = CORRECT_ANSWERS[user_id]
    counter = 0
    for i,j in enumerate(answers):
        if int(answers[j]) == correct_answers[i]:
            counter += 1

    return str(counter)


@app.route('/profile/<username>')
def profile(username):
    return render_template('home2.html', item={'username': username})

if __name__ == '__main__':
    app.run(port=3001)
