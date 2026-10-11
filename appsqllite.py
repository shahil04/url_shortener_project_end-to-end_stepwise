import random
import sqlite3
import string
from pathlib import Path

from flask import Flask, g, redirect, render_template, request

app = Flask(__name__)
DATABASE = Path(__file__).with_name("url_shortener.db")


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = sqlite3.connect(DATABASE)
    try:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                short_code TEXT NOT NULL UNIQUE,
                long_url TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                click_count INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        db.commit()
    finally:
        db.close()


def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None
    if request.method == "POST":
        long_url = request.form["long_url"]
        db = get_db()
        while True:
            code = generate_code()
            try:
                db.execute(
                    "INSERT INTO urls (short_code, long_url) VALUES (?, ?)",
                    (code, long_url),
                )
                db.commit()
                break
            except sqlite3.IntegrityError:
                if db.execute(
                    "SELECT 1 FROM urls WHERE short_code = ?", (code,)
                ).fetchone():
                    continue
                raise

        short_url = request.host_url + code

    return render_template("index.html", short_url=short_url)


@app.route("/<code>")
def redirect_url(code):
    db = get_db()
    result = db.execute(
        "SELECT long_url FROM urls WHERE short_code = ?", (code,)
    ).fetchone()

    if result is None:
        return "URL not found", 404

    db.execute(
        "UPDATE urls SET click_count = click_count + 1 WHERE short_code = ?",
        (code,),
    )
    db.commit()
    return redirect(result["long_url"])


init_db()


if __name__ == "__main__":
    app.run()
