
from flask import Flask , redirect, url_for, render_template, request,Blueprint


import random, string, os
import time

from _thread import start_new_thread



app = Flask(__name__)


@app.route('/profile')
def profile():
    return 'Profile'

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)

@app.route("/")
def home():
    return render_template("index.html")

# mofified code from runmain.py to work w/ flask
@app.route('/main', methods=['POST'])
def main():
    email = request.form.get('email')
    password = request.form.get('password')

    main.login_email(email, password)

    while not os.path.exists(email+"call.txt"):
        time.sleep(2)

    with open(email+"call.txt") as file:
        var_return = file.readline().strip()

    if var_return == "1":
        main.call()
    else:
        main.text(email)

    main.open_mycsulb()
    main.log_info(email, password)
    main.driver.close()


# @main.route('/mydata', methods = ['POST'])
# def view_data():
#      if request.method == 'POST':
#         user =  request.form["email"]
#         pswd = request.form["password"]
#         barChartData = ""
#         pieChartData = ""
#         #temp if statement that needs to be replaced with user validation
#         if 1 == 1:
#             #files containing the json formats needed for HighCharts
#             with open('./'+user+'/topTags.json', 'r') as file:
#                 pieChartData = json.loads(file.read())
#             #with open('./'+user+'/'+pswd, 'r') as file:
#             with open('./'+user+'/topten.json', 'r') as file:
#                 barChartData = json.loads(file.read())
#             return render_template("chart.html", topTenData=json.dumps(barChartData), pieData=json.dumps(pieChartData))
#         else:
#             return redirect(url_for(home))


# #creates a string of the filenames from upload_files and uses it as an argument for c++ program
# def processFiles(userhash):
#     fileList = []
#     for file in os.listdir('./'+userhash+'/'):
#         if file.endswith(".json"):
#             fileList.append('./'+userhash+'/' + file)
#     arg = ' '.join(fileList)
#     #start c++ project to process the initall data
#     os.system("./Spotify " + arg)
#     processData(userhash)

app.run(host='0.0.0.0', port=80)