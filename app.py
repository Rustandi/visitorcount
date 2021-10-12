# compose_flask/app.py
import flask
from redis import Redis

app = flask.Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    # redis.incr('hits')
    # return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')
    ip_address = flask.request.remote_addr
    visits = redis.incr('counter')
    return "User address: {} Hits: {}".format(ip_address, visits)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)