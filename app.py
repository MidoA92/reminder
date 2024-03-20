from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'reminder'
 
mysql = MySQL(app)




@app.route("/")
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM reminder")
    reminders = cursor.fetchall() 
    cursor.close()
    return render_template("home.html", reminders=reminders)




@app.route("/add-reminder", methods=['GET', 'POST'])
def addReminder():

    title= request.form.get('title')
    time=request.form.get('time')
    description=request.form.get('description')

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO reminder (name, time, description) VALUES (%s, %s, %s)", (title, time, description))
    mysql.connection.commit()
    cursor.close()

    return redirect('/')


app.run(debug=True)