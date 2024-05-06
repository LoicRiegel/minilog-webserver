"""Example code that a web client could use to get and send logs to the server.

Assuming that the server is currently running on localhost, on port 5000.
"""

from pprint import pprint

import requests

HOST = "http://localhost"
PORT = 5000
BASE_URL = f"{HOST}:{PORT}"
LOGS_ROUTE = f"{BASE_URL}/logs"


# Get all the received logs
assert LOGS_ROUTE == "http://localhost:5000/logs"
resp = requests.get(LOGS_ROUTE)
if resp.ok:
    print("GET response:")
    pprint(resp.json())
else:
    print(f"GET request to {LOGS_ROUTE} failed with status {resp.status_code}")


# Get all the received logs
new_logs = {
    "logs": [
        "test log 1",
        "test log 2",
        "test log 3",
    ]
}
resp = requests.post(LOGS_ROUTE, json=new_logs)
if resp.ok:
    print("POST response:")
    pprint(resp.json())
else:
    print(f"POST request to {LOGS_ROUTE} failed with status {resp.status_code}")

# Delete all logs
resp = requests.delete(LOGS_ROUTE, json=new_logs)
if resp.ok:
    print("DELETE response:")
    pprint(resp.json())
else:
    print(f"DELETE request to {LOGS_ROUTE} failed with status {resp.status_code}")
