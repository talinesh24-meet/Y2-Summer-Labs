from flask import Flask

app = Flask(__name__)

@app.route('/home')
    def home():
        return '''<html>
<h1>mediterranean food</h1>
<p>Welcome to the home page </p>
<imag src="https://domesticfits.com/wp-content/uploads/2023/05/lebanese-food-300x170.jpg"></img>
<imag src="https://www.highpointscientific.com/media/magefan_blog/AstroHub-WhatIsOuterSpace.jpg"></img>
<imag src="https://www.highpointscientific.com/media/magefan_blog/AstroHub-WhatIsOuterSpace.jpg"></img>



    </html>'''
if __name__ == '__main__':
    app.run(debug=True)
