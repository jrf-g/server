import flask
app = flask.Flask(__name__)
@app.route("/")
def home():
    return flask.render_template("form.html")
@app.route("/submit", methods=["POST"])
def submit():
    name = flask.request.form["articlebar"]
    return flask.redirect(f"/wiki/{name}")
@app.route("/wiki/<articlename>")
def home():
    if articlename = "form":
        return "going here will break the site. you cannot continue"
    return render_template(f"{articlename}.html")
