from flask import Flask, render_template, request, redirect, url_for
import pymysql
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")


def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )


def init_db():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS maintenance_requests (
                id INT AUTO_INCREMENT PRIMARY KEY,
                tenant_name VARCHAR(100) NOT NULL,
                unit_number VARCHAR(20) NOT NULL,
                building_name VARCHAR(100) NOT NULL,
                issue_category VARCHAR(50) NOT NULL,
                priority VARCHAR(20) NOT NULL,
                description TEXT NOT NULL,
                preferred_visit_date DATE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    conn.commit()
    conn.close()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    tenant_name = request.form["tenant_name"]
    unit_number = request.form["unit_number"]
    building_name = request.form["building_name"]
    issue_category = request.form["issue_category"]
    priority = request.form["priority"]
    description = request.form["description"]
    preferred_visit_date = request.form["preferred_visit_date"]

    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO maintenance_requests
            (tenant_name, unit_number, building_name, issue_category, priority, description, preferred_visit_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            tenant_name,
            unit_number,
            building_name,
            issue_category,
            priority,
            description,
            preferred_visit_date
        ))
    conn.commit()
    conn.close()

    return redirect(url_for("dashboard"))


@app.route("/dashboard")
def dashboard():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM maintenance_requests
            ORDER BY created_at DESC
        """)
        requests_data = cursor.fetchall()
    conn.close()
    return render_template("dashboard.html", requests=requests_data)


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)