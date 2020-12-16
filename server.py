from flask import Flask, Response, request, render_template
import database_funcs
from flask import Flask, render_template, request, redirect
import database_funcs as df
from trivia.triv_api import get_question, CORRECT_ANSWERS
from trivia.triv_ranks import get_top_5, get_top_5_of_all_categories, get_top_5_same_user

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')


@app.route('/')
def home():
    return render_template('home.html')


@app.route("/sign_up", methods=['POST'])
def add_user():
    name = request.form.get("UserName")
    password = request.form.get("psw")
    result = database_funcs.check_user_name(name)
    if not result:
        database_funcs.add_user(name, password)
        return render_template('home2.html', item={'username': name})
    else:
        return render_template('sign_up.html')


@app.route("/rankings/<category>")
def ranking(category):
    ranks = get_top_5(category)
    print(ranks)
    return render_template('rankings.html', ranks=ranks)
    pass


@app.route("/log-in", methods=['POST'])
def check_user():
    name = request.form.get("UserName")
    password = request.form.get("psw")
    result = database_funcs.check_user(name, password)
    if result:
        return render_template('home2.html', item={'username': name})
    else:
        return render_template('log-in.html')


@app.route('/profile/<username>/quiz/<category>')
def quiz(username, category):
    user_id = df.get_user_id(username)
    result = get_question(id=user_id, category=category, type='multiple')
    return render_template('quiz.html', item=result, username=username, category=category)


@app.route('/profile/<username>/quiz/<category>/checkAnswers', methods=['POST'])
def check(username, category):
    user_id = df.get_user_id(username)
    answers = request.form
    correct_answers = CORRECT_ANSWERS[user_id]
    counter = 0
    for i, j in enumerate(answers):
        if int(answers[j]) == correct_answers[i]:
            counter += 1
    database_funcs.add_score(user_id, category, counter)
    if counter > 5:
        return render_template('score.html',gif='https://media2.giphy.com/media/vLruErVSYGx8s/giphy.gif',score=counter,name=username)
    else:
        return render_template('score.html',gif='https://www.icegif.com/wp-content/uploads/buzz-lightyear-feeling-dumb.gif',score=counter,name=username)


@app.route('/profile/<username>')
def profile(username):
    user_id = database_funcs.get_user_id(username)
    user_top5 = get_top_5_same_user(user_id)  # send to html page
    print(user_top5)
    top_5 = get_top_5_of_all_categories()

    dict_ = {}
    for item in top_5:
        for key, val in item.items():
            dict_[key] = val
    top_5 = dict_

    return render_template('home2.html', item={'username': username}, sports=top_5.get('Sports'),
                           politics=top_5.get('Politics'), celebrities=top_5.get('Celebrities'),
                           history=top_5.get('History'))


if __name__ == '__main__':
    app.run(port=3001)
