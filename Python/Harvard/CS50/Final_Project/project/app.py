from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from random import seed, randint
from helpers import login_required
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///wordle.db")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        number_of_letters = request.form.get("letters")

        if not number_of_letters:
            flash("Must choose number of letters")
            return render_template("index.html")

        if len(db.execute("SELECT * FROM user_info WHERE user_id = ?", session.get("user_id"))) == 0:
            db.execute("INSERT INTO user_info (user_id, points, current_letter, current_level, current_row) VALUES (?, ?, ?, ?, ?)", session.get("user_id"), 0, int(number_of_letters), 1, 1)

        else:
            db.execute("UPDATE user_info SET current_letter = ? WHERE user_id = ?", int(number_of_letters), session.get("user_id"))

        return redirect("/levels")

    else:
        return render_template("index.html")


@app.route("/levels", methods=["GET", "POST"])
@login_required
def levels():
    if request.method == "POST":
        level = request.form.get("level")
        current_letter = db.execute("SELECT current_letter FROM user_info WHERE user_id = ?", session.get("user_id"))
        current_level = db.execute("SELECT current_level FROM user_info WHERE user_id = ?", session.get("user_id"))

        if not level:
            flash("Must choose a level")
            levels = []
            counter = 1

            for _ in range(1000):
                levels.append(counter)
                counter += 1

            return render_template("levels.html", current_letter=current_letter[0]["current_letter"], levels=levels, current_level=current_level[0]["current_level"])

        if int(level) > current_level[0]["current_level"]:
            flash("You haven't unlocked this level yet")
            levels = []
            counter = 1

            for _ in range(1000):
                levels.append(counter)
                counter += 1

            return render_template("levels.html", current_letter=current_letter[0]["current_letter"], levels=levels, current_level=current_level[0]["current_level"])

        db.execute("UPDATE user_info SET current_level = ? WHERE user_id = ?", int(level), session.get("user_id"))
        return redirect("/level")

    else:
        current_letter = db.execute("SELECT current_letter FROM user_info WHERE user_id = ?", session.get("user_id"))
        current_level = db.execute("SELECT current_level FROM user_info WHERE user_id = ?", session.get("user_id"))
        levels = []
        counter = 1

        for _ in range(1000):
            levels.append(counter)
            counter += 1

        return render_template("levels.html", current_letter=current_letter[0]["current_letter"], levels=levels, current_level=current_level[0]["current_level"])


@app.route("/level", methods=["GET", "POST"])
@login_required
def level():
    if request.method == "POST":
        current_letter = db.execute("SELECT current_letter FROM user_info WHERE user_id = ?", session.get("user_id"))
        current_level = db.execute("SELECT current_level FROM user_info WHERE user_id = ?", session.get("user_id"))
        current_row = db.execute("SELECT current_row FROM user_info WHERE user_id = ?", session.get("user_id"))
        seed(current_level[0]["current_level"])

        match current_letter[0]["current_letter"]:
            case 5:
                random_number = randint(1, 1000)
                random_word = db.execute("SELECT five_letters FROM words WHERE id = ?", random_number)
                status = ["wrong","wrong","wrong","wrong","wrong","wrong","wrong","wrong"]

                letters = []
                counter = 1
                for _ in range(current_letter[0]["current_letter"]):
                    if not request.form.get(f"l{counter}"):
                        flash("Must fill in all the blanks")
                        return redirect("/level")

                    letters.append(request.form.get(f"l{counter}").lower())
                    counter += 1

                for random_counter, random_letter in enumerate(random_word[0]["five_letters"]):
                    for user_counter, user_letter in enumerate(letters):
                        if random_letter in user_letter:
                            if random_counter == user_counter:
                                status[user_counter] = "exact"

                            elif status[user_counter] not in "exact":
                                status[user_counter] = "close"

                points = 0
                for letter in status:
                    if letter in "exact":
                        points += 1

                won = 1
                if points == current_letter[0]["current_letter"]:
                    db.execute("UPDATE user_info SET current_level = current_level + 1, points = points + 10, current_row = 1 WHERE user_id = ?", session.get("user_id"))
                    won = 2
                    return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=status, letters=letters, won=won)

                else:
                    db.execute("UPDATE user_info SET current_row = current_row + 1 WHERE user_id = ?", session.get("user_id"))

                if current_row[0]["current_row"] == 5 and won != 2:
                    db.execute("UPDATE user_info SET current_row = 1 WHERE user_id = ?", session.get("user_id"))
                    won = 3
                    return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=status, letters=letters, won=won)

                return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=status, letters=letters, won=won)

            case 6:
                random_number = randint(1, 1000)
                random_word = db.execute("SELECT six_letters FROM words WHERE id = ?", random_number)
                status = ["wrong","wrong","wrong","wrong","wrong","wrong","wrong","wrong"]

                letters = []
                counter = 1
                for _ in range(current_letter[0]["current_letter"]):
                    if not request.form.get(f"l{counter}"):
                        flash("Must fill in all the blanks")
                        return redirect("/level")

                    letters.append(request.form.get(f"l{counter}").lower())
                    counter += 1

                for random_counter, random_letter in enumerate(random_word[0]["six_letters"]):
                    for user_counter, user_letter in enumerate(letters):
                        if random_letter in user_letter:
                            if random_counter == user_counter:
                                status[user_counter] = "exact"

                            elif status[user_counter] not in "exact":
                                status[user_counter] = "close"

                points = 0
                for letter in status:
                    if letter in "exact":
                        points += 1

                won = 1
                if points == current_letter[0]["current_letter"]:
                    db.execute("UPDATE user_info SET current_level = current_level + 1, points = points + 10, current_row = 1 WHERE user_id = ?", session.get("user_id"))
                    won = 2
                    return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=status, letters=letters, won=won)

                else:
                    db.execute("UPDATE user_info SET current_row = current_row + 1 WHERE user_id = ?", session.get("user_id"))

                if current_row[0]["current_row"] == 5 and won != 2:
                    db.execute("UPDATE user_info SET current_row = 1 WHERE user_id = ?", session.get("user_id"))
                    won = 3
                    return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=status, letters=letters, won=won)

                return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=status, letters=letters, won=won)

            case 7:
                random_number = randint(1, 1000)
                random_word = db.execute("SELECT seven_letters FROM words WHERE id = ?", random_number)
                status = ["wrong","wrong","wrong","wrong","wrong","wrong","wrong","wrong"]

                letters = []
                counter = 1
                for _ in range(current_letter[0]["current_letter"]):
                    if not request.form.get(f"l{counter}"):
                        flash("Must fill in all the blanks")
                        return redirect("/level")

                    letters.append(request.form.get(f"l{counter}").lower())
                    counter += 1

                for random_counter, random_letter in enumerate(random_word[0]["seven_letters"]):
                    for user_counter, user_letter in enumerate(letters):
                        if random_letter in user_letter:
                            if random_counter == user_counter:
                                status[user_counter] = "exact"

                            elif status[user_counter] not in "exact":
                                status[user_counter] = "close"

                points = 0
                for letter in status:
                    if letter in "exact":
                        points += 1

                won = 1
                if points == current_letter[0]["current_letter"]:
                    db.execute("UPDATE user_info SET current_level = current_level + 1, points = points + 10, current_row = 1 WHERE user_id = ?", session.get("user_id"))
                    won = 2
                    return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=status, letters=letters, won=won)

                else:
                    db.execute("UPDATE user_info SET current_row = current_row + 1 WHERE user_id = ?", session.get("user_id"))

                if current_row[0]["current_row"] == 5 and won != 2:
                    db.execute("UPDATE user_info SET current_row = 1 WHERE user_id = ?", session.get("user_id"))
                    won = 3
                    return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=status, letters=letters, won=won)

                return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=status, letters=letters, won=won)

            case 8:
                random_number = randint(1, 1000)
                random_word = db.execute("SELECT eight_letters FROM words WHERE id = ?", random_number)
                status = ["wrong","wrong","wrong","wrong","wrong","wrong","wrong","wrong"]

                letters = []
                counter = 1
                for _ in range(current_letter[0]["current_letter"]):
                    if not request.form.get(f"l{counter}"):
                        flash("Must fill in all the blanks")
                        return redirect("/level")

                    letters.append(request.form.get(f"l{counter}").lower())
                    counter += 1

                for random_counter, random_letter in enumerate(random_word[0]["eight_letters"]):
                    for user_counter, user_letter in enumerate(letters):
                        if random_letter in user_letter:
                            if random_counter == user_counter:
                                status[user_counter] = "exact"

                            elif status[user_counter] not in "exact":
                                status[user_counter] = "close"

                points = 0
                for letter in status:
                    if letter in "exact":
                        points += 1

                won = 1
                if points == current_letter[0]["current_letter"]:
                    db.execute("UPDATE user_info SET current_level = current_level + 1, points = points + 10, current_row = 1 WHERE user_id = ?", session.get("user_id"))
                    won = 2
                    return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=status, letters=letters, won=won)

                else:
                    db.execute("UPDATE user_info SET current_row = current_row + 1 WHERE user_id = ?", session.get("user_id"))

                if current_row[0]["current_row"] == 5 and won != 2:
                    db.execute("UPDATE user_info SET current_row = 1 WHERE user_id = ?", session.get("user_id"))
                    won = 3
                    return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=status, letters=letters, won=won)

                return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=status, letters=letters, won=won)

    else:
        db.execute("UPDATE user_info SET current_row = 1 WHERE user_id = ?", session.get("user_id"))
        current_letter = db.execute("SELECT current_letter FROM user_info WHERE user_id = ?", session.get("user_id"))
        current_row = db.execute("SELECT current_row FROM user_info WHERE user_id = ?", session.get("user_id"))
        match current_letter[0]["current_letter"]:
            case 5:
                return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=[" "," "," "," "," "], letters=["","","","",""], won=1)
            case 6:
                return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=[" "," "," "," "," "," "], letters=["","","","","",""], won=1)
            case 7:
                return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=[" "," "," "," "," "," "," "], letters=["","","","","","",""], won=1)
            case 8:
                return render_template("level.html", current_letter=current_letter[0]["current_letter"], current_row=current_row[0]["current_row"], status=[" "," "," "," "," "," "," "," "], letters=["","","","","","","",""], won=1)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            flash("Must provide username")
            return render_template("register.html")

        for usernames in db.execute("SELECT username FROM users"):
            if username in usernames["username"]:
                flash("Username already in use")
                return render_template("register.html")

        if not password:
            flash("Must provide password")
            return render_template("register.html")

        if password != confirmation:
            flash("Password doesn't match")
            return render_template("register.html")

        password = generate_password_hash(password)

        db.execute("INSERT INTO users (username, password) VALUES (?, ?)", username, password)
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username:
            flash("Must provide username")
            return render_template("login.html")

        if not password:
            flash("Must provide password")
            return render_template("login.html")

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(rows) != 1 or not check_password_hash(rows[0]["password"], password):
            flash("Invalid username and/or password")
            return render_template("login.html")

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
