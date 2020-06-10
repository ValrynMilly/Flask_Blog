from application import app
from flask import render_template


dummyData = [
{
"name": {"first":"Smash", "last":"Mouth"},
"title":"All Star",
"content":"Somebody once told me the world is gonna roll me"
"\n I ain't the sharpest tool in the shed"
"\n She was looking kind of dumb with her finger and her thumb"
"\n In the shape of an ""L"" on her forehead"
},
{
"name": {"first":"Monty", "last":"Python"},
"title":"Herring",
"content":"when you have found the shrubbery, you must cut down the mightiest tree in the forest... with... a herring!"
},
{
"name": {"first":"Jules", "last":"Winnfield"},
"title":"Big Kahuna Burger",
"content":"Do you know why they call it a royale with cheese? Because of the Metric System? CHECK OUT THE BIG BRAIN ON BRETT"
}
]

@app.route('/')
@app.route('/home')
def home():
<<<<<<< HEAD
    postData = Posts.query.all()
=======
>>>>>>> parent of f4e70fa... stage 3
    return render_template('home.html', title='Home', posts=dummyData)

@app.route('/about')
def about():
    return render_template('about.html', title='about')
@app.route('/register')
def register():
    return render_template('register.html', title='Register')
@app.route('/login')
def login():
    return render_template('login.html', title='Login')

