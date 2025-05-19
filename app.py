from flask import Flask, render_template
import os

app = Flask(name)

@app.route("/")
def index():
    return render_template("index.html")

if name == "main":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
