"""Entry point of the web server application."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world() -> None:
    """Home route."""
    return "<p>Hello, World!</p>"
