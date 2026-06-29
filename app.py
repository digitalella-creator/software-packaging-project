from flask import Flask
from config import DEBUG

app = Flask(__name__)
app.config["DEBUG"] = DEBUG

@app.route("/")
def home():
    return "Software Packaging Project Successful!"

if __name__ == "__main__":
    app.run()