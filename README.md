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


## Contributing

Use **pre-commit hooks** which will run the ``ruff`` linter and formatter, and run the ``mypy`` type-checker:
```sh
pre-commit install
```
