from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenido a Bounsic Backend"

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

