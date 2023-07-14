import requests
import json
import time

start = time.time()
url = "http://127.0.0.1:8080/generate"
data = {
    "prompt": "Asteroids are",
    "stream": True,
    "n": 1,
    "temperature": 0,
    "best_of": 1
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers, stream=True)

# Get the raw byte stream and decode it into a string, then split on null character
responses = response.content.decode('utf-8').split('\0')
#print(responses)

for resp in responses:
    if resp:  # Ignore any empty strings from splitting
        parsed = json.loads(resp)
        print(parsed)
        end = time.time()
        print(end-start)
        #break