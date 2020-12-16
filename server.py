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