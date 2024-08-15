from app import create_app
from flask import flask,request,render_template

app = Flask(__name__)

@app.route("/")

def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True)