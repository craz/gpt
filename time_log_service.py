from datetime import datetime, timedelta
import calendar
from typing import List, Dict, Any, Set

from bitrix_client import BitrixClient


class TimeLogService:

main
    def __init__(self, client: BitrixClient) -> None:
        self.client = client

    @staticmethod
    def month_date_range(year: int, month: int) -> tuple[datetime, datetime]:

        main
        start = datetime(year, month, 1)
        last_day = calendar.monthrange(year, month)[1]
        end = datetime(year, month, last_day, 23, 59, 59)
        return start, end

    @staticmethod
    def add_months(date: datetime, months: int) -> datetime: