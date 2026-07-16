import json
import urllib.request
import urllib.error
from datetime import datetime
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Send JSON payload to server")
    parser.add_argument('--topic', default='topicB')
    parser.add_argument('--key', default='titles')
    parser.add_argument('--value', default='quit!')
    parser.add_argument('--url', default='http://localhost:8000/')
    parser.add_argument('--dry-run', action='store_true', help='Print JSON and exit without sending')
    args = parser.parse_args()

    req_data = {
        "topic": args.topic,
        "key": args.key,
        "value": args.value,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    }

    data = json.dumps(req_data).encode('utf-8')

    if args.dry_run:
        print("Dry run: prepared JSON:")
        print(json.dumps(req_data, ensure_ascii=False, indent=2))
        return

    url = args.url

    req = urllib.request.Request(
        url,
        data=data,
        headers={'content-type': 'application/json'},
        method='POST'
    )

    try:
        with urllib.request.urlopen(req) as response:
            status = response.getcode()
            if status == 200:
                print("send data successfully!")
            else:
                print(status)
                
    except urllib.error.HTTPError as e:
        print(e.code)
    except urllib.error.URLError as e:
        print(f"Failed to reach server: {e.reason}")


if __name__ == "__main__":
    main()
