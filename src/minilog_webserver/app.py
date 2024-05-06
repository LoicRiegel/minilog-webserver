"""Entry point of the web server application."""

from flask import Flask, abort, jsonify, render_template, request

app = Flask(__name__)


received_logs: list[str] = []


@app.route("/logs", methods=["GET", "POST", "DELETE"])
def logs():
    """Expose the received logs."""
    match request.method:
        case "DELETE":
            received_logs.clear()
            return "", 200
        case "POST":
            try:
                new_logs = request.json["logs"]
            except KeyError:
                abort(400)
            received_logs.extend(new_logs)
            return "", 201
        case "GET":
            return jsonify({"logs": received_logs})


@app.route("/")
def hello_world():
    """Home route that displays the logs."""
    return render_template("log_page.html")
