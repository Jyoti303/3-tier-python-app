from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "http://backend:5000"

@app.route('/')
def index():
    response = requests.get(f"{API_URL}/quotes")
    quotes = response.json()
    return render_template('index.html', quotes=quotes)

@app.route('/add', methods=['POST'])
def add_quote():
    quote = request.form['quote']
    requests.post(f"{API_URL}/quotes", json={"quote": quote})
    return redirect('/')

