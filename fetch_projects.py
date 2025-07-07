"""Export Bitrix24 projects to a JSON file."""

import argparse
import json
from typing import List, Dict, Any

from dotenv import load_dotenv
from bitrix.client import BitrixClient
import requests


def fetch_all_projects(
    client: BitrixClient, *, page_size: int = 50
) -> List[Dict[str, Any]]:
    """Return all projects using the REST API."""

    projects: List[Dict[str, Any]] = []
    page = 1
    while True:
        payload = {
            "ORDER": {"ID": "ASC"},
            "FILTER": {},
            "SELECT": ["*"],
            "NAV_PARAMS": {"nPageSize": page_size, "iNumPage": page},
        }
        try:
            data = client.call("sonet_group.get", payload)
        except requests.RequestException as exc:
            raise RuntimeError(f"Request failed: {exc}") from exc

        result = data.get("result")
        if isinstance(result, list):
            projects.extend(result)
        else:
            break

        if not data.get("next"):
            break
        page += 1

    return projects


def main() -> None:
    parser = argparse.ArgumentParser(description="Export Bitrix24 projects")
    parser.add_argument("output", help="Path to save the projects JSON")
    parser.add_argument(
        "--webhook-url",
        help="Bitrix24 webhook base URL (overrides WEBHOOK_URL env variable)",
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=50,
        help="Number of projects to request per page (default: 50)",
    )
    args = parser.parse_args()

    load_dotenv()
    client = BitrixClient(args.webhook_url)
    print("Fetching projects...")
    projects = fetch_all_projects(client, page_size=args.page_size)
    print(f"Fetched {len(projects)} projects")

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(projects, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
