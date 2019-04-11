from flask import Flask, render_template
import os

FORMAT = "https://storage.googleapis.com/static_a/staticA/css/home.css"
app = Flask(__name__)

# static_folder=os.path.join('https://storage.googleapis.com/static_a/'


# app.config['STATIC_FOLDER'] = "https://storage.googleapis.com/static_a/staticA/"

@app.route('/')
def home():
    return render_template("home.html", FORMAT=FORMAT)

if __name__ == '__main__':
    app.run(debug = True)

