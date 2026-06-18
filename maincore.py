import flask
app = flask.Flask(__name__)
@app.route("/")
def home():
    return flask.render_template("form.html")
@app.route("/submit", methods=["POST"])
def submit():
    name = flask.request.form["articlebar"]
    return f"finding articles related to {name}..."
@app.route("/wiki/<articlename>")
def home():
    return render_template(f"{articlename}.html")
