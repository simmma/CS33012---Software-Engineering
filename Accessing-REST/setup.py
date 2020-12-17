# python -m pip install requests
import requests
user = "simmma"
resp = requests.get('https://api.github.com/users/' + user)
print(resp)
if resp.status_code != 200:
    # This means something went wrong.
    # raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    print("oops")
else:
    print(resp.json())