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

3. Run the script. Use `--year` and `--month` to specify the starting month.
   Set `--months` to span multiple months (default is 2) and pass `--show-projects` to print
   the list of active projects for the selected period.

```bash
python main.py --year 2025 --month 6 --months 2 --show-projects
```

The command above prints all time log entries for June and July 2025 and shows
the IDs of projects with any activity during that period.

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
