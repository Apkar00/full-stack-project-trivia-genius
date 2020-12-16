from flask import Flask, render_template, request, redirect
import database_funcs as df
from triv_api import get_question, CORRECT_ANSWERS

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')


@app.route('/')
def root():
    return render_template('home.html')


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
    app.run(port=3000)
