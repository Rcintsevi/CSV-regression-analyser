from flask import Flask, request, send_file, render_template,jsonify,send_from_directory
import os
from regression import run_regression

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/plots/<filename>")
def serve_plot(filename):
    return send_from_directory("tmp/plots", filename)


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

    result=run_regression(path,weight,bias,alpha,iterations)

    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)

