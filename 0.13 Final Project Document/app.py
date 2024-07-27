from flask import Flask,render_template,request,redirect,url_for
from flask import session as login_session 
import pyrebase
import requests
import json

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

API_KEY = 'your_amadeus_api_key'
API_URL = 'https://test.api.amadeus.com/v1/reference-data/locations/pois'


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
        if password != confirm_password:
            error = "Passwords do not match"
            print(error)
            return render_template("error.html", error=error)
            try:
                login_session['users'] = auth.create_user_with_email_and_password(email, password)
                user_id = login_session['users']['localId']
                db.child('users').set({
                "email" : email,
                "username" : username,
                "password": password
                
                })
                return redirect(url_for('home'))
            except Exception as e:
                error = str(e)
                print(error)
                return render_template("error.html", error=error)
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
        except Exception as e:
            error = str(e)
            print(error)
            return render_template('error.html', error=error)
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
 

@app.route('/results', methods=['POST', 'GET'])
def results():
    if request.method == 'POST':
        continent = request.form['continent']
        activity = request.form['activity']
        budget = request.form['budget']
        query_params = {
        'continent': continent,
        'activity': activity,
        'budget': budget
        }

        all_destinations = [
            {
                'name': 'Paris, France',
                'continent': 'Europe',
                'activity': 'Sightseeing',
                'budget': 'Medium',
                'image_url': 'https://static01.nyt.com/images/2023/06/22/multimedia/22hours-paris-tjzf/22hours-paris-tjzf-master1050.jpg',
                'description': 'Experience the romance and history of Paris with its iconic landmarks and vibrant culture.'
            },
            {
                'name': 'Kyoto, Japan',
                'continent': 'Asia',
                'activity': 'Cultural',
                'budget': 'Medium',
                'image_url': 'https://www.hertz.com/content/dam/hertz/global/blog-articles/planning-a-trip/kyoto-japan/kyoto-header.jpg',
                'description': 'Discover the ancient temples and beautiful gardens of Kyoto, a city steeped in tradition.'
            },
            {
                'name': 'Verbier , Switzerland',
                'continent': 'Africa',
                'activity': 'Adventure',
                'budget': 'High',
                'image_url': 'https://static.independent.co.uk/2023/07/13/16/iStock-467335200.jpg?quality=75&width=1250&crop=3%3A2%2Csmart&auto=webp',
                'description': 'Explore the stunning landscapes and diverse wildlife of Cape Town, a city of natural beauty.'
            },
            {
                'name': 'Cochabamba ,Bolivia',
                'continent': 'South America',
                'activity': 'chilling',
                'budget': 'High',
                'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Cristo_de_La_Concordia.jpg/435px-Cristo_de_La_Concordia.jpg',
                'description': 'Explore the stunning landscapes and diverse wildlife of Cape Town, a city of natural beauty.'
            },
            {
                'name': 'Cairns ,Australia',
                'continent': 'Australia',
                'activity': 'Coast',
                'budget': 'Medium',
                'image_url': 'https://tropicalnorthqueensland.org.au/wp-content/uploads/Four-Mile-Beach_Flagstaff-Hill-1024x682.jpg',
                'description': 'Explore the stunning landscapes and diverse wildlife of Cape Town, a city of natural beauty.'
            }
            ]
        filtered_destinations = [destination for destination in all_destinations if destination['continent'] == continent or destination['activity'].lower() in activity.lower() or destination['budget'].lower() in budget.lower()]
        return render_template('results.html', destinations=filtered_destinations)



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