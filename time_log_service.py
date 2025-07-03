from datetime import datetime, timedelta
import calendar
from typing import List, Dict, Any, Set

from bitrix_client import BitrixClient


class TimeLogService:
    def __init__(self, client: BitrixClient) -> None:
        self.client = client

    @staticmethod
    def month_date_range(year: int, month: int) -> tuple[datetime, datetime]:
        start = datetime(year, month, 1)
        last_day = calendar.monthrange(year, month)[1]
        end = datetime(year, month, last_day, 23, 59, 59)
        return start, end

    @staticmethod
    def add_months(date: datetime, months: int) -> datetime:
        year = date.year + (date.month - 1 + months) // 12
        month = (date.month - 1 + months) % 12 + 1
        day = min(date.day, calendar.monthrange(year, month)[1])
        return date.replace(year=year, month=month, day=day)

    def fetch_time_logs(self, start_date: datetime, end_date: datetime, page_size: int = 50) -> List[Dict[str, Any]]:
        logs: List[Dict[str, Any]] = []
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
            data = self.client.call('task.elapseditem.getlist', payload)
            logs.extend(data.get('result', []))
            if not data.get('next'):
                break
            page += 1
        return logs

    def get_active_projects(self, start_date: datetime, end_date: datetime) -> Set[int]:
        logs = self.fetch_time_logs(start_date, end_date)
        task_ids = {log['TASK_ID'] for log in logs if 'TASK_ID' in log}
        projects: Set[int] = set()
        for task_id in task_ids:
            payload = {'taskId': task_id, 'select': ['ID', 'GROUP_ID']}
            data = self.client.call('tasks.task.get', payload)
            task = data.get('result', {}).get('task')
            if task and 'GROUP_ID' in task:
                try:
                    projects.add(int(task['GROUP_ID']))
                except (ValueError, TypeError):
                    continue
        return projects

    def compute_range(self, year: int, month: int, months: int) -> tuple[datetime, datetime]:
        start, _ = self.month_date_range(year, month)
        end = self.add_months(start, months)
        end -= timedelta(seconds=1)
        return start, end
