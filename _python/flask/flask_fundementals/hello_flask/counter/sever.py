from flask import Flask, render_template, session
from werkzeug.utils import redirect
app = Flask(__name__)
app.secret_key = 'keep it safe'


@app.route("/")
def counter():
    if 'start' not in session:
        session['start'] = 0
    session['start'] += 1
    return render_template('index.html', visits=str(session["start"]))

@app.route('/add')
def add():
    session['start'] += 1
    return redirect("/")

@app.route('/destroy')
def clear():
    session.clear()
    return redirect("/")


if __name__ == '__main__':
    app.run()
