from flask import Flask, render_template

app = Flask(__name__,template_folder='/templates')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/welcome', strict_slashes=False)
def welcome():
    return render_template("welcome.html")

if __name__ == '__main__':
    app.run(debug=True)
