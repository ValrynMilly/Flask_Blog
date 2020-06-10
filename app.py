from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Flask Stage 1: Testing simple output & Making sure flask runs and is operative, currently running on localhost"