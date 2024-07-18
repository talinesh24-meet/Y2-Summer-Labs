from flask import Flask,render_template
import random

app = Flask(__name__,template_folder="template")

@app.route('/')
def home():
	return render_template("home.html")
@app.route('/fortune')
def fortune():
	possible_fortunes=["Great joy is coming.","A surprise awaits.","Luck is on your side.","You will find love.","Success is near.","New beginnings soon.","Happiness is yours.","A friend needs you.","Expect good news.","You will be blessed."]
	return render_template("fortune.html",possible_fortunes=possible_fortunes)

@app.route('/indecisive')
def indecisive():
    indecisive_fortunes = random.randint(0,11)  
    return render_template('indecisive.html', fortunes=indecisive_fortunes)

@app.route('/magic')
def magic():
    return render_template('magic.html')

@app.route('/response')
def response():
    choice = random.randint(1, 3)
    return render_template('response.html', choice=choice)
    


if __name__ == '__main__':
    app.run(debug=True)