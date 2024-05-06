"""Entry point of the web server application."""

from flask import Flask, jsonify, render_template

app = Flask(__name__)


received_logs: list[str] = [
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 - 1",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 - 2",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 - 3",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
    "127.0.0.1 - - [06/May/2024 10:17:46] GET /favicon.ico HTTP/1.1 404 -",
]


@app.route("/logs", methods=["GET"])
def logs():
    """Route to expose the received logs."""
    return jsonify({"logs": received_logs})


@app.route("/")
def hello_world():
    """Home route that displays the logs."""
    return render_template("log_page.html", messages=received_logs)
