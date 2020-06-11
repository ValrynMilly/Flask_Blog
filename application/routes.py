from application import app, db, bcrypt
from application.models import Posts, Users
from application.forms import PostForm, RegistrationForm
from flask import render_template, redirect, url_for
from application import app, db
from application.forms import PostForm



@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        postData = Posts(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                title = form.title.data,
                content = form.content.data
        )

        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('post.html', title='Post', form=form)
    return render_template("post.html", posts=[])    

@app.route('/')
@app.route('/home')
def home():
    postData = Posts.query.all()
    return render_template('home.html', title='Home', posts=postData)

@app.route('/about')
def about():
    return render_template('about.html', title='about')
@app.route('/register')
def register():
    return render_template('register.html', title='Register')
@app.route('/login')
def login():
    return render_template('login.html', title='Login')

