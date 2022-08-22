from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Yeeeeey"
if __name__ == "__main__";
app.run (debug=True)
