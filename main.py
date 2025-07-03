import argparse
from dotenv import load_dotenv

from bitrix_client import BitrixClient
from time_log_service import TimeLogService


def main() -> None:
    """Entry point for the CLI."""
    parser = argparse.ArgumentParser(description='Fetch Bitrix24 time logs')
    parser.add_argument('--year', type=int, default=2025, help='Start year')
    parser.add_argument('--month', type=int, default=6, help='Start month (1-12)')
    parser.add_argument('--months', type=int, default=1, help='Number of months to include')
    parser.add_argument('--show-projects', action='store_true', help='Print list of active projects')
    args = parser.parse_args()

    load_dotenv()
    client = BitrixClient()
    service = TimeLogService(client)

    start_date, end_date = service.compute_range(args.year, args.month, args.months)
    logs = service.fetch_time_logs(start_date, end_date)
    for log in logs:
        print(log)

    if args.show_projects:
        projects = service.get_active_projects(start_date, end_date)
        print('Active projects:', sorted(projects))


if __name__ == '__main__':
    main()

