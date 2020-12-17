# python -m pip install requests
import requests

url = "https://api.github.com/"

def checkStatus(resp):
    if resp.status_code != 200:
        print("oops")
        return -1
    return 0

def basicAPICall():
    # First call to github API
    resp = requests.get(url)
    if(checkStatus(resp)):
        return ""
    return resp.text

def getUser(user):
    # Get list of repos of a passed user
    userReq = "users/" + user
    resp = requests.get(url + userReq)
    if(checkStatus(resp)):
        return ""
    return resp.text
    
def main():
    # print(basicAPICall())
    print(getUser("simmma"))

main()
