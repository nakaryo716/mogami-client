import json
import urllib.request
import urllib.error

def main():
    req_data = {
        "topic": "topicA",
        "key": "test-key",
        "value": "this is test value",
        "timestamp": "2020-07-14 22:48:00.345678"
    }

    url = "http://localhost:8000/"
    
    data = json.dumps(req_data).encode('utf-8')
    
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
                print("send data successfly!")
            else:
                print(status)
                
    except urllib.error.HTTPError as e:
        print(e.code)
    except urllib.error.URLError as e:
        print(f"Failed to reach server: {e.reason}")


if __name__ == "__main__":
    main()
