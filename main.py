from flask import *
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('Key')
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("index.html")

@app.route('/css/')
def css():
  return send_file("static/style.css")


@app.route('/bootstrap/')
def boot():
  return send_file("static/bootstrap.min.css")

@app.route('/js/')
def js():
  return send_file("static/main.js")

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

@app.errorhandler(500)
def overload(e):
  return render_template("500.html")

@app.route('/500')
def test500():
  return render_template("500.html")


app.run(host='0.0.0.0', port=81)