from flask import Flask,render_template,url_for,redirect,request
from flask import session
import pyrebase

app = Flask(__name__,template_folder="templates",static_folder='static')

Config = {
  "apiKey": "AIzaSyDGarSTibNmc8OmVEameK9AjpbhY8p8tSs",
  "authDomain": "auth-lab-9db17.firebaseapp.com",
  "projectId": "auth-lab-9db17",
  "storageBucket": "auth-lab-9db17.appspot.com",
  "messagingSenderId": "58834721290",
  "appId": "1:58834721290:web:562e60a8763676dc6e1df3",
  "measurementId": "G-MPFP3BS75R",
  "databaseURL": "https://auth-lab-9db17-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
app.config['SECRET_KEY'] = 'super-secret-key' 

@app.route('/',methods=['GET', 'POST'])
def signup():
  
  if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       session['quotes'] = []
       try:
          session['user'] = auth.create_user_with_email_and_password(email, password)
          return redirect('/home')
       except:
           error = "Authentication failed"
           print(error)
           return render_template("error.html")
  else:
      return render_template("signup.html")


@app.route('/signin',methods=['GET', 'POST'])
def signin():
  if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       session['quotes'] = []
       try:
          login_session['user'] = auth.sign_in_with_email_and_password(email, password)
          return redirect(url_for('home'))
       except:
           error = "Authentication failed"
           print(error)
           redirect('/error')

  return render_template("signin.html")


@app.route('/signout',methods=['GET', 'POST'])
def signout():
  auth.signOut()
  session['user'] = None
  return redirect(url_for('signin'))



@app.route('/home',methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
      quote = request.form['quote']

      session['quotes'].append(quote)

      session.modified = True

      return redirect(url_for('thanks'))
    else:

      redirect('signup')
      return render_template("home.html")

   


@app.route('/display',methods=['GET', 'POST'])
def display():
  return render_template("display.html",quotes = session['quotes'])

@app.route('/thanks',methods=['GET', 'POST'])
def thanks():
  return render_template('thanks.html')

@app.route('/error',methods=['GET', 'POST'])
def error():
  return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)