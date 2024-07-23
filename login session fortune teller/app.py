from flask import Flask,render_template
from flask import session as login_session 
import random

app = Flask(__name__,template_folder="template")


possible_fortunes=["Great joy is coming.","A surprise awaits.","Luck is on your side.","You will find love.","Success is near.","New beginnings soon.","Happiness is yours.","A friend needs you.","Expect good news.","You will be blessed."]



@app.route('/',methods=['POST','GET'])
def home():
	return render_template("home.html", name =login_session["name"])

@app.route('/fortune')
def fortune():
    if len(login_session["birthday"])<10:
        fortune1=possible_fortunes[len(login_session["birthday"])]
        return render_template("fortune.html",possible_fortunes=fortune1, name=login_session["name"])
    else:
        return render_template('birthdaymnth.html')

# @app.route('/indecisive')
# def indecisive():
#     indecisive_fortunes = random.randint(0,11)  #picks a random index.
#     return render_template('indecisive.html', fortunes=indecisive_fortunes)

@app.route('/magic')
def magic():
    return render_template('magic.html')

@app.route('/response')
def response():
    choice = random.randint(1, 3)
    return render_template('response.html', choice=choice)
    
@app.route('/login',methods=['POST','GET']))
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        login_session["birthday"]=request.form["birthday"]
        login_session["name"]=request.form["name"]
        return redirect(url_for('home'))

    

if __name__ == '__main__':
    app.run(debug=True)