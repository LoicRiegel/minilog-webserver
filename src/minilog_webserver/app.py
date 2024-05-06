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
        case "POST":
            try:
                new_logs = request.json["logs"]
            except KeyError:
                abort(400, f"""Received invalid JSON! Use format {"logs": ["log 1", "log2", ...]}""")
            received_logs.extend(new_logs)
    return jsonify({"logs": received_logs})


@app.route("/")
def hello_world():
    """Home route that displays the logs."""
    return render_template("log_page.html")
