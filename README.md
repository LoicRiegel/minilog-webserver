# ``minilog`` web server (demo project)

Web server that can be used to receive logs sent with the HTTP logger of the minilog library.

## Install

```sh
git clone
cd minilog-webserver
pip install .
```

## Usage

The following command will start a web server on localhost, port 5000:
```sh
python -m minilog_webserver
```
Then, open http://127.0.0.1:5000 in any browser.

The server exposes a single endpoint: **"/logs"**.

Look at [this example](./examples/usage_by_client.py) for how to use the endpoint as a client.

### The "logs" endpoint

Get all the logs received until now:
```sh
curl http://localhost:5000/logs
```

Add new logs:
```sh
curl -H 'Content-Type: application/json' \
      -d '{ "logs": ["log 1", "log 2", "log 2"] }' \
      -X POST \
      https://localhost:5000/logs
```

CLear all received logs:
```sh
curl +X DELETE http://localhost:5000/logs
```

## Contributing

Use **pre-commit hooks** which will run the ``ruff`` linter and formatter, and run the ``mypy`` type-checker:
```sh
pre-commit install
```
