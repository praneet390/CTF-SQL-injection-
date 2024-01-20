from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)


users = {'admin': 'user0', 'user1': 'user2', 'user2': 'admin2'}


db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="passwd",
    database="ctf"
)

@app.route('/', methods=['GET'])
def home():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']

        
        


        
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            
            return f"Database Login successful! Welcome, {username}."
        else:
            return "Login failed! Please check your username and password."

    
    return render_template('web.html')


@app.route('/login', methods=['POST'])
def home1():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']

        
        


        
        cursor = db.cursor(buffered=True)
        query = "select * from users where username='"+username +"' " + " and " + " password=" + "'" +  password +  "'"
        result=''
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            print('statment=',query)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print('username=',username)
            print('password=',password)
            print('statment=',query)
        finally:
    
            cursor.close()
            

        print(result)
        if result:
            
            return f"Database Login successful! Welcome, {username}."
        else:
            return "Login failed! Please check your username and password."

    
    return render_template('web.html')

if __name__ == '__main__':
    app.run(debug=True)
