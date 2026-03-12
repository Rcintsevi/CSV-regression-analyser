from flask import Flask, request, send_file, render_template
import os
from regression import run_regression

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


UPLOAD_FOLDER="uploads"
os.makedirs(UPLOAD_FOLDER,exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload():

    if "file" not in request.files:
        return "No file uploaded"


    file=request.files["file"]
    path=os.path.join(UPLOAD_FOLDER,file.filename)

    file.save(path)

    plot_path=run_regression(path)

    return send_file(plot_path, mimetype="image/png")

if __name__=="__main__":
    app.run(debug=True)

