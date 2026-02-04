from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)
FILE = "students.xlsx"

if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Name", "Email", "Event"])
    df.to_excel(FILE, index=False)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        df = pd.read_excel(FILE)
        df.loc[len(df)] = [
            request.form["name"],
            request.form["email"],
            request.form["event"]
        ]
        df.to_excel(FILE, index=False)
    return render_template("register.html")

@app.route("/view")
def view():
    df = pd.read_excel(FILE)
    return render_template("view.html", rows=df.values)

if __name__ == "__main__":
    app.run()
