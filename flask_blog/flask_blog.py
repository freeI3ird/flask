from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '15dc16666c6d1557cc699e726076b3b2'

dummyPosts = [
    {
        'author': 'Manish Rathi',
        'title': 'Artificial Intelligence',
        'content': 'AI and ML First Post',
        'date_posted': 'August 9, 2020',
    },
    {
        'author': 'fit_bird',
        'title': 'General Fitness',
        'content': 'Fitness content Second Post',
        'date_posted': 'August 9, 2020',
    },
]


@app.route("/") 	# both route call the same function
@app.route("/home")
def home_page():
    # return render_template("home.html")
    # This name posts will be available in the context of template, and it contains the data of dummyPosts
    return render_template("home.html", posts=dummyPosts)


@app.route("/about")
def about_page():
    return render_template("about.html", title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    print("Enter the Register function")
    form = RegistrationForm()   # If enduser has sent some data using POST, then that data is used to create form or
    # fields of form will have the enduser data otherwise form will be created with data in fields = None
    print(form.username, form.username.data)
    print(form.password, form.password.data)
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for("home_page"))
        pass
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
