# Bitrix24 Time Log Fetcher

This repository contains a small example script for fetching time log entries from Bitrix24 via the REST API.

## Usage

1. Copy `.env.example` to `.env` and update the values:

```
cp .env.example .env
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

## Docker

An alternative way to run the script is using Docker.

1. Build the image:

```bash
docker build -t timelog-fetcher .
```

2. Run the container with the Bitrix24 webhook URL passed via the `WEBHOOK_URL` environment variable:

```bash
docker run --rm -e WEBHOOK_URL=https://<your_portal>.bitrix24.ru/rest/<user_id>/<webhook_key>/ timelog-fetcher
```
