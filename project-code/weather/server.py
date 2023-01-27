"""
Main module of the server file
"""

from flask import Flask, render_template, jsonify
import connexion

# Create the application instance
#app = Flask(__name__, template_folder = "template")

app = connexion.App(__name__, specification_dir = "./")
app.add_api("../services/weather.yaml")

# Read the yaml file to configure the endpoints
#app.add_api("cpu.yaml")

# create a URL route in our application for "/"
@app.route("/weather")
def home():
    return render_template("home.html")


def main():
    app.run(host = "0.0.0.0", port = 5000, debug=True)


if __name__ == "__main__":
    main()

