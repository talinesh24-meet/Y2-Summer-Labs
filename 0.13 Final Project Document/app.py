from flask import Flask,render_template,request,redirect,url_for
from flask import session as login_session 
import pyrebase

app = Flask(__name__,template_folder="templates",static_folder="static")

Config = {
  "apiKey": "AIzaSyCDgrlx4JpX3nDm_jEp1TKw-V5jCg8Qcgc",
  "authDomain": "project-71b9a.firebaseapp.com",
  "projectId": "project-71b9a",
  "storageBucket": "project-71b9a.appspot.com",
  "messagingSenderId": "773480904710",
  "appId": "1:773480904710:web:1458abe9b80025a6106b87",
  "measurementId": "G-X1MTF43LBG",
  "databaseURL": "https://project-71b9a-default-rtdb.firebaseio.com/"
}

# trip={
# "privTrip":
#     {"PeoplePerroom":
#      {"one": 1
#     "two":2
#     "three": 3},
#     "Countries":
#     {"Switzerland":"ski",
#     "Japan":"Mountains",
#     "Jordan":"CitiesArea"},
#     "Budget":
#     {"below2000":"LowQuality"
#     "2000-3000":"Average"
#     "Over3000":"GoodTrip"}
#     }
# }




firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
app.config['SECRET_KEY'] = 'super-secret-key' 
db=firebase.database()

@app.route('/',methods=['POST','GET'])
def signup():
    if request.method == 'POST':
       email = request.form['email']
       username = request.form['username']
       password = request.form['password']
       confirm_password = request.form['confirm_password']
       try:
          login_session['users'] = auth.create_user_with_email_and_password(email, password)
          user_id = login_session['users']['localId']
          db.child('users').set({
            "email" : email,
            "username" : username,
            "password": password,
            "confrim_password": confirm_password
            })

          if password==confirm_password:
            return redirect(url_for('home'))
          else:
            error = "Authentication failed"
            print(error)
            return render_template("error.html")
       except:
           error = "Authentication failed"
           print(error)
           return render_template("error.html")
    else:
        return render_template("signup.html")




@app.route('/signin',methods=['POST','GET'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # session['quotes'] = []
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
            print(error)
            render_template('error.html')
    else:
        return render_template("signin.html")

@app.route('/signout',methods=['POST','GET'])
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))

@app.route('/private',methods=['POST','GET'])
def private():
    return render_template("private.html")

# @app.route('/submit_survey', methods=['POST','GET'])
# def submit_survey():
#     continent = request.form['continent']
#     activity = request.form['activity']
#     budget = request.form['budget']
#     return redirect(url_for('results', continent=continent, activity=activity, budget=budget))

# @app.route('/results')
# def results():
#     continent = request.args.get('continent')
#     activity = request.args.get('activity')
#     budget = request.args.get('budget')
#     return render_template('results.html', continent=continent, activity=activity, budget=budget)
 

@app.route('/results')
def results():
    destinations = [
        {
            'name': 'Paris, France',
            'image_url': 'https://example.com/paris.jpg',
            'description': 'Experience the romance and history of Paris with its iconic landmarks and vibrant culture.'
        },
        {
            'name': 'Kyoto, Japan',
            'image_url': 'https://example.com/kyoto.jpg',
            'description': 'Discover the ancient temples and beautiful gardens of Kyoto, a city steeped in tradition.'
        },
        {
            'name': 'Cape Town, South Africa',
            'image_url': 'https://example.com/capetown.jpg',
            'description': 'Explore the stunning landscapes and diverse wildlife of Cape Town, a city of natural beauty.'
        }
    ]
    return render_template('results.html', destination1=destinations[0], destination2=destinations[1], destination3=destinations[2])
 

@app.route('/home', methods=['POST','GET'])
def home():
    return render_template("home.html")

@app.route('/solo',methods=['POST','GET'])
def solo():
    return render_template("solo.html")
@app.route('/group',methods=['POST','GET'])
def group():
    return render_template("group.html")

@app.route('/preferences',methods=['POST','GET'])
def preferences():
    return render_template("preferences.html")
@app.route('/contact',methods=['POST','GET'])
def contact():
    return render_template("contact.html")   

 

   

    

if __name__ == '__main__':
    app.run(debug=True)