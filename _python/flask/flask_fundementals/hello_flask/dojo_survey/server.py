from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

@app.route("/")
def flask():
    return render_template("index.html")

    
@app.route("/result", methods=["POST"])
def result():
    name_from_form = request.form["name"]
    location_from_form = request.form["locations"]
    languange_from_form = request.form["language"]
    comment_from_form = request.form["comments"]
    return render_template("result.html", name_temp=name_from_form, location_temp=location_from_form, language_temp=languange_from_form, comment_temp= comment_from_form)
if __name__ == '__main__':
   app.run()