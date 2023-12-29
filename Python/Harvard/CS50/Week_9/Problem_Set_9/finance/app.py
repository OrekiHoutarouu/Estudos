import os

from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

app = Flask(__name__)

app.jinja_env.filters["usd"] = usd

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    if (
        len(
            db.execute(
                "SELECT * FROM purchases WHERE user_id = ?", session.get("user_id")
            )
        )
        > 0
    ):
        rows = {}
        extra = {}
        placeholders = []

        for row in db.execute(
            "SELECT symbol, shares FROM purchases WHERE user_id = ? GROUP BY symbol ORDER BY date",
            session.get("user_id"),
        ):
            values = lookup(row["symbol"])
            rows["symbol"] = row["symbol"]
            rows["shares"] = row["shares"]
            rows["price"] = usd(values["price"])
            rows["total"] = usd(values["price"] * rows["shares"])
            placeholders.append(rows.copy())

        user_cash = db.execute(
            "SELECT cash FROM users WHERE id = ?", session.get("user_id")
        )
        extra["balance"] = usd(user_cash[0]["cash"])
        extra["grand"] = usd(
            (values["price"] * rows["shares"]) + (user_cash[0]["cash"])
        )
        placeholders.append(extra)
        return render_template("index.html", placeholders=placeholders)

    else:
        return render_template("index.html", placeholders=" ")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        values = lookup(symbol)
        shares = request.form.get("shares")
        user_cash = db.execute(
            "SELECT cash FROM users WHERE id = ?", session.get("user_id")
        )

        if not values:
            return apology("symbol doesn't exists")

        try:
            if int(shares) < 0:
                raise ValueError
        except ValueError:
            return apology("shares number must be a positive integer")

        if (values["price"] * int(shares)) > user_cash[0]["cash"]:
            return apology("not enough cash to afford this amount of shares")

        for symbols in db.execute(
            "SELECT symbol FROM purchases WHERE user_id = ?", session.get("user_id")
        ):
            if symbol == symbols["symbol"]:
                db.execute(
                    "UPDATE purchases SET shares = shares + ? WHERE symbol = ? AND user_id = ?",
                    shares,
                    symbol,
                    session.get("user_id"),
                )
                db.execute(
                    "INSERT INTO transactions (type, symbol, shares, price, date, user_id) VALUES (?, ?, ?, ?, ?, ?)",
                    "purchase",
                    symbol,
                    int(shares),
                    values["price"],
                    datetime.now(),
                    session.get("user_id"),
                )
                db.execute(
                    "UPDATE users SET cash = cash - ? WHERE id = ?",
                    (values["price"] * int(shares)),
                    session.get("user_id"),
                )
                return redirect("/")

        db.execute(
            "INSERT INTO purchases (symbol, shares, price, date, user_id) VALUES (?, ?, ?, ?, ?)",
            symbol,
            int(shares),
            values["price"],
            datetime.now(),
            session.get("user_id"),
        )
        db.execute(
            "INSERT INTO transactions (type, symbol, shares, price, date, user_id) VALUES (?, ?, ?, ?, ?, ?)",
            "purchase",
            symbol,
            int(shares),
            values["price"],
            datetime.now(),
            session.get("user_id"),
        )
        db.execute(
            "UPDATE users SET cash = cash - ? WHERE id = ?",
            (values["price"] * int(shares)),
            session.get("user_id"),
        )

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    if (
        len(
            db.execute(
                "SELECT * FROM transactions WHERE user_id = ?", session.get("user_id")
            )
        )
        > 0
    ):
        rows = {}
        placeholders = []

        for row in db.execute(
            "SELECT * FROM transactions WHERE user_id = ? ORDER BY date",
            session.get("user_id"),
        ):
            rows["type"] = row["type"].capitalize()
            rows["symbol"] = row["symbol"]
            rows["shares"] = row["shares"]
            rows["price"] = usd(row["price"])
            rows["date"] = row["date"]
            placeholders.append(rows.copy())

        return render_template("history.html", placeholders=placeholders)

    else:
        return render_template("history.html", placeholders=" ")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 403)

        elif not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    session.clear()

    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        values = lookup(symbol)
        if not values:
            return apology("symbol doesn't exists", 400)

        price = usd(values["price"])

        return render_template("quoted.html", values=values, price=price)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        has_number = False
        has_symbol = False

        if not username:
            return apology("must provide username")

        for usernames in db.execute("SELECT username FROM users"):
            if username in usernames["username"]:
                return apology("username already in use")

        if not password:
            return apology("must provide password")

        for char in password:
            if char.isnumeric():
                has_number = True
            elif not char.isalnum():
                has_symbol = True

        if has_number == False or has_symbol == False or len(password) < 8:
            return apology(
                "Password must contain numbers, symbols and be at least 8 digits long"
            )

        elif password != confirmation:
            return apology("password doesn't match")

        password = generate_password_hash(password)

        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)", username, password
        )

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        values = lookup(symbol)
        shares = request.form.get("shares")

        if not values:
            return apology("symbol doesn't exists")

        if not shares:
            return apology("shares number must be a positive integer")

        try:
            if int(shares) < 0:
                raise ValueError
        except ValueError:
            return apology("shares number must be a positive integer")

        user_shares = db.execute(
            "SELECT shares FROM purchases WHERE symbol = ? AND user_id = ?",
            symbol,
            session.get("user_id"),
        )

        if int(shares) > user_shares[0]["shares"]:
            return apology("you don't own that amount of shares of this stock")

        db.execute(
            "UPDATE purchases SET shares = shares - ? WHERE symbol = ? AND user_id = ?",
            shares,
            symbol,
            session.get("user_id"),
        )
        db.execute(
            "INSERT INTO transactions (type, symbol, shares, price, date, user_id) VALUES (?, ?, ?, ?, ?, ?)",
            "sale",
            symbol,
            int(shares),
            values["price"],
            datetime.now(),
            session.get("user_id"),
        )
        db.execute(
            "UPDATE users SET cash = cash + ? WHERE id = ?",
            (values["price"] * int(shares)),
            session.get("user_id"),
        )
        return redirect("/")

    else:
        user_stocks = db.execute(
            "SELECT symbol FROM purchases WHERE user_id = ?", session.get("user_id")
        )
        return render_template("sell.html", stocks=user_stocks)
