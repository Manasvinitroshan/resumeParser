from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@app.route("/")
def resume():
    return render_template('resume.html')

@app.route("/pred",methods=["POST","GET"])

def pred():
    if request.method == 'POST':


if __name__ == '__main__':
    app.run(debug=True)