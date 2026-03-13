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
    weight=float(request.form["weight"])
    bias=float(request.form["bias"])
    alpha=float(request.form["alpha"])
    iterations=int(request.form["iterations"])
    path=os.path.join(UPLOAD_FOLDER,file.filename)

    file.save(path)

    plot_path=run_regression(path,weight,bias,alpha,iterations)

    return send_file(plot_path, mimetype="image/png")

if __name__=="__main__":
    app.run(debug=True)

