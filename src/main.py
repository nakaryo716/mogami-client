import argparse
import json
import urllib.error
from lib import Client


def main():
    parser = argparse.ArgumentParser(description="Send JSON payload to server")
    parser.add_argument('--topic', default='topicB')
    parser.add_argument('--key', default='titles')
    parser.add_argument('--value', default='quit!')
    parser.add_argument('--url', default='http://localhost:8000/')
    parser.add_argument('--dry-run', action='store_true', help='Print JSON and exit without sending')
    args = parser.parse_args()

    client = Client(url=args.url)

    if args.dry_run:
        payload = client.post(args.topic, args.key, args.value, dry_run=True)
        print("Dry run: prepared JSON:")
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    try:
        status = client.post(args.topic, args.key, args.value, dry_run=False)
        if status == 200:
            print("send data successfully!")
        else:
            print(status)
    except urllib.error.URLError as e:
        print(f"Failed to reach server: {e.reason}")


if __name__ == "__main__":
    main()
