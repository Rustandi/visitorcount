import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    ip_address = flask.request.remote_addr
    return "User address: " + ip_address

app.run(host="0.0.0.0", port=80)