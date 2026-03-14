# homework_bot

`homework_bot` ist ein Telegram-Bot in Python, der den Status von Yandex-Practicum-Hausaufgaben über die API überwacht und bei Änderungen automatisch Benachrichtigungen in einen Telegram-Chat sendet.

## Funktionsweise

Der Bot läuft in einer Endlosschleife und führt regelmäßig folgende Schritte aus:

1. Abrufen der neuesten Daten vom Practicum-Endpunkt.
2. Validieren der API-Antwortstruktur.
3. Prüfen des Hausaufgabenstatus (`approved`, `reviewing`, `rejected`).
4. Senden einer Nachricht an den angegebenen Telegram-Chat.

Bei Fehlern schreibt der Bot Logs und versucht, eine Fehlermeldung ebenfalls per Telegram zu senden.

## Voraussetzungen

- Python 3.9+
- Telegram-Bot-Token
- Zugang zur Yandex-Practicum-API

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Konfiguration

Lege eine `.env`-Datei im Projektverzeichnis an und definiere:

```env
PRACTICUM_TOKEN=dein_practicum_token
TELEGRAM_TOKEN=dein_telegram_bot_token
TELEGRAM_CHAT_ID=deine_chat_id
```

## Start

```bash
python homework.py
```

## Tests

```bash
pytest
```

## Projektstruktur

- `homework.py` — Hauptlogik des Bots.
- `messages.py` — Textkonstanten für Logs und Fehler.
- `exceptions.py` — Eigene Exception-Klassen.
- `tests/` — automatisierte Tests.

## Hinweise

- Das Polling-Intervall ist über `RETRY_TIME` (standardmäßig 600 Sekunden) definiert.
- Für Deployment ist eine `Procfile`-Konfiguration enthalten (`worker: python homework.py`).
