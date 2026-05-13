from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="myapp_base"
        )

        cursor = db.cursor()
        cursor.execute("SELECT 'MySQL Connected Successfully!'")
        result = cursor.fetchone()

        return result[0]

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)