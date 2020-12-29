from flask import Flask
app = Flask(__name__)


@app.route("/") 	# both route call the same function
@app.route("/home")
def helloWorld():
    return "<h1>helloWorld</h1>"


@app.route("/about")
def aboutPage():
    return "<h1>author = freeBird</h1>"


if __name__ == "__main__":
    app.run(debug=True)
