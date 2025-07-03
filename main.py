import requests
import calendar
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

WEBHOOK_BASE = os.getenv('WEBHOOK_URL')
if not WEBHOOK_BASE:
    raise RuntimeError('WEBHOOK_URL not found in .env')

WEBHOOK_URL = WEBHOOK_BASE.rstrip('/') + '/task.elapseditem.getlist.json'

YEAR = 2025
MONTH = 6


def get_month_date_range(year: int, month: int):
    start = datetime(year, month, 1)
    last_day = calendar.monthrange(year, month)[1]
    end = datetime(year, month, last_day, 23, 59, 59)
    return start, end


def fetch_time_logs(start_date, end_date, page_size=50):
    logs = []
    page = 1
    while True:
        payload = [
            {},
            {
                '>=CREATED_DATE': start_date.strftime('%Y-%m-%d'),
                '<=CREATED_DATE': end_date.strftime('%Y-%m-%d')
            },
            ['ID', 'TASK_ID', 'USER_ID', 'CREATED_DATE', 'SECONDS'],
            {'NAV_PARAMS': {'nPageSize': page_size, 'iNumPage': page}}
        ]
        resp = requests.post(WEBHOOK_URL, json=payload, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        logs.extend(data.get('result', []))
        if not data.get('next'):
            break
        page += 1
    return logs


def main():
    start_date, end_date = get_month_date_range(YEAR, MONTH)
    logs = fetch_time_logs(start_date, end_date)
    for log in logs:
        print(log)


if __name__ == '__main__':
    main()
