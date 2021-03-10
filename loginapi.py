from flask import Flask,render_template,redirect,session,url_for,jsonify,request

import psycopg2
import psycopg2.extras
import sys
from configparser import ConfigParser


DB_Host = "127.0.0.1" 
DB_name = "myfirstdatabase"
DB_user = "postgres"
DB_pass = "ranchi1357"

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET','POST'])
def index():
    conn = psycopg2.connect(
        host = DB_Host, database = DB_name, user = DB_user, password = DB_pass)

    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            print (username)
            print(password)

            print(type(username))
            print(type(password))
            cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
            cur.execute("select * from loginInfo where emailid = %s and password = %s",(username,password))
            info = cur.fetchone()
            print(info)
            print (info['emailid'])
            print (info['password'])
            print (type(info['emailid']))
            print (type(info['password']))

            if info is not None:
                if info['emailid'] == username and info['password'] == password :
                    return "login Successfull"
                else:
                    return "login Unsuccessfull, please Register"
            
            
    
    return render_template("login.html")


    conn.commit()

    cur.close()

    conn.close()



if __name__ == '__main__':
    app.run(debug = True) 
