# Bitrix24 Project Fetcher

This repository contains a minimal script for retrieving a single project from Bitrix24 via the REST API and saving it to a JSON file.

## Usage

1. Copy `.env.example` to `.env` and update the `WEBHOOK_URL` value.

```bash
cp .env.example .env
```

2. Install the dependencies in a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the script, passing the desired output path:

```bash
python main.py project.json
```

The file `project.json` will contain the first project returned by Bitrix24.

## Docker

You can also run the script using Docker:

```bash
docker build -t project-fetcher .
docker run --rm -e WEBHOOK_URL=https://<portal>.bitrix24.ru/rest/<user_id>/<webhook_key>/ project-fetcher project.json
```
