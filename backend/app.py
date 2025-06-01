from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='db',
        user='root',
        password='example',
        database='quotes_db'
    )

@app.route('/quotes', methods=['GET'])
def get_quotes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT quote FROM quotes")
    quotes = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return jsonify(quotes)

@app.route('/quotes', methods=['POST'])
def add_quote():
    new_quote = request.json['quote']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO quotes (quote) VALUES (%s)", (new_quote,))
    conn.commit()
    cursor.close()
    conn.close()
    return '', 201

