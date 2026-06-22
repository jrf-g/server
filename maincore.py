import flask, time, os
app = flask.Flask(__name__)
enabled = True
poweringdown = False
blacklist = set()
@app.before_request
def pre():
    if flask.request.remote_addr in blacklist:
        return "Anti-bot handling triggered", 403
    elif not enabled:
        return "", 503
@app.route("/")
def redirect():
    return flask.redirect("/home")
@app.route("/home")
def home():
    return flask.render_template("form.html")
@app.route("/submit", methods=["POST"])
def submit():
    name = flask.request.form["articlebar"]
    return flask.redirect(f"/wiki/{name}")
@app.route("/wiki/<articlename>")
def wiki():
    if articlename == "form" or articlename == "editor":
        blacklist.add(flask.request.remote_addr)
        return "You might break this page. sorry!", 403
    path = f"{articlename}.html"
    if os.path.isfile(f"templates/{path}"):
        return "", 404
    return flask.render_template(path)
@app.route("/edit")
def editfile():
    name = flask.request.form["articlebar"]
    if name == "form" or name == "editor":
        blacklist.add(flask.request.remote_addr)
        return "You might break this page. sorry!", 403
    newcontent = flask.request.form["newcontent"]
    with open(f"templates/{name}.html", 'w', encoding='utf-8') as file:
        file.write(f"<html><head><title>article: {name}</title></head><body>{newcontent}</body></html>")
    return "", 204
@app.route("/editor")
def showeditor():
    return flask.render_template("editor.html")
def quit():
    poweringdown = True
    time.sleep(4)
    poweringdown = False
    enabled = False
def serverboot():
    enabled = True
@app.route("/status")
def statcheck():
    localstatus = not poweringdown
    return flask.jsonify({shuttingoff: not localstatus})
@app.route("/banlist")
def bancheck():
    return flask.jsonify(blacklist)
