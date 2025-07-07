import argparse
import json
from dotenv import load_dotenv

from bitrix.client import BitrixClient


def main() -> None:
    """Fetch a single project from Bitrix24 and save it to a file."""
    parser = argparse.ArgumentParser(description="Fetch one Bitrix24 project")
    parser.add_argument("output", help="Path to output JSON file")
    args = parser.parse_args()

    load_dotenv()
    client = BitrixClient()
    payload = {
        "ORDER": {"ID": "ASC"},
        "FILTER": {},
        "SELECT": ["*"],
        "NAV_PARAMS": {"nPageSize": 1, "iNumPage": 1},
    }
    data = client.call("sonet_group.get", payload)
    result = data.get("result", [])

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
