from flask import Flask, render_template, url_for
app = Flask(__name__)

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
def hello_world():
    # return render_template("home.html")
    # This name posts will be available in the context of template, and it contains the data of dummyPosts
    return render_template("home.html", posts=dummyPosts)


@app.route("/about")
def about_page():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
