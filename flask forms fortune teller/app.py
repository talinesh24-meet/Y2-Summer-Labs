from flask import Flask,render_template,url_for,redirect,request
import random

app = Flask(__name__,template_folder="template")

@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        birth=request.form['name']
        return redirect(url_for('fortune',birthMonth=birth))
        #return render_template("fortune.html")
    #return render_template("fortune.html")

@app.route('/fortune/<birthMonth>')
def fortune(birthMonth):
    possible_fortunes=["Great joy is coming.","A surprise awaits.","Luck is on your side.","You will find love.","Success is near.","New beginnings soon.","Happiness is yours.","A friend needs you.","Expect good news.","You will be blessed."]
    # ssrandom_num = random.randint(0,9)
    len_of_month = len(birthMonth)
    if len_of_month < 10:
        fortune2 = possible_fortunes[len_of_month]

    else:
        fortune2 = "unavailable"

    return render_template("fortune.html", fortune = fortune2)

# @app.route('/indecisive')
# def indecisive():
#     indecisive_fortunes = random.randint(0,11)  
#     return render_template('indecisive.html', fortunes=indecisive_fortunes)

# @app.route('/magic')
# def magic():
#     return render_template('magic.html')

# @app.route('/response')
# def response():
#     choice = random.randint(1, 3)
#     return render_template('response.html', choice=choice)
    


if __name__ == '__main__':
    app.run(debug=True)