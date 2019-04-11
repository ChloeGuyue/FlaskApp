from flask import Flask, render_template
import os

FORMAT = "staticB"
app = Flask(__name__, static_folder=os.path.join(os.getcwd(), FORMAT))


app.config['STATIC_FOL DER'] = FORMAT

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug = True)

