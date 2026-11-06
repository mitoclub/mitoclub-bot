# Dependency maintenance

Use Python 3.12 (see `.python-version`); Python 3.6 is no longer supported by the updated HTTP dependencies. The deprecated Heroku `runtime.txt` is replaced by `.python-version`, allowing current patch releases.

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip check
python -m unittest discover -s tests -v
```

Tests use a mocked Telegram transport and do not poll Telegram, send real messages, or access Google Sheets. A live deployment still needs the existing external `config.py` and valid credentials; test the deployment separately before enabling scheduled reminders.

The unused third-party `datetime` package was removed; Python includes `datetime` in the standard library.

PyTelegramBotAPI is updated to 4.37.1 because 2.2.3 uses the now-reserved `async` identifier and cannot even import on modern Python. Existing synchronous handlers, `send_message`, and `polling` remain in use.
