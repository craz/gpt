import argparse
import json
from dotenv import load_dotenv
from bitrix.client import BitrixClient


def fetch_all_projects(client: BitrixClient) -> list[dict]:
    """Return all projects using the REST API."""
    projects: list[dict] = []
    page = 1
    while True:
        payload = {
            'ORDER': {'ID': 'ASC'},
            'FILTER': {},
            'SELECT': ['*'],
            'NAV_PARAMS': {'nPageSize': 50, 'iNumPage': page},
        }
        data = client.call('sonet_group.get', payload)
        result = data.get('result')
        if isinstance(result, list):
            projects.extend(result)
        else:
            break
        if not data.get('next'):
            break
        page += 1
    return projects


def main() -> None:
    parser = argparse.ArgumentParser(description='Export Bitrix24 projects')
    parser.add_argument('output', help='Path to save the projects JSON')
    args = parser.parse_args()

    load_dotenv()
    client = BitrixClient()
    projects = fetch_all_projects(client)

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(projects, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
