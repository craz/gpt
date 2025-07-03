# Bitrix24 Time Log Fetcher

This repository contains a small example script for fetching time log entries from Bitrix24 via the REST API.

## Usage

1. Create a `.env` file in the project root with the following content:

```
WEBHOOK_URL=https://<your_portal>.bitrix24.ru/rest/<user_id>/<webhook_key>/
```

2. Install the dependencies in a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the script:

```bash
python main.py
```

The script prints all time log entries for June 2025 using the `task.elapseditem.getlist` method.
