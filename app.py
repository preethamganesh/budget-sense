# Copyright © 2023 Preetham Ganesh.


import os
import sys


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_PATH)


from flask import Flask, render_template


# Initializes flask app.
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index() -> str:
    """Renders template for 'index.html'.

    Renders template for 'index.html'.

    Args:
        None.

    Returns:
        A string for the rendered template for 'signup.html'.
    """
    return render_template("index.html")


if __name__ == "__main__":
    print()
    app.run(host="0.0.0.0", port=3000, debug=True)
