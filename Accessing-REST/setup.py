# python -m pip install requests
import requests
import json

url = "https://api.github.com/"
user = "simmma"
token = ""  # Enter valid token here!

def checkStatus(resp):
    if resp.status_code != 200:
        print("oops")
        print(resp.json()["message"])
        return -1
    return 0

def basicAPICall(args):
    # First call to github API
    resp = requests.get(url + args)
    if(checkStatus(resp)):
        return ""
    return resp

def getUserPublicRepos():
    # Get list of public repo names of a passed user
    userReq = "users/" + user + "/repos"
    resp = requests.get(url + userReq)
    if(checkStatus(resp)):
        return ""
    #print(type(resp.content)) # class 'bytes'
    #print(type(resp.json())) # class 'list'
    #print(type(resp.json()[0])) # class 'dict'
    resp = resp.json()
    names = [];
    for i in range(len(resp)):
        names.append(resp[i]['name'])
    return names

def getUserAllRepos():
    if token == "":
        print("Please enter a valid token!")
        return 
    resp = requests.get(url + "search/repositories?q=user:" + user, auth=(user, token))
    if(checkStatus(resp)):
        return ""
    #resp = resp.json()
    items = resp.json()["items"]
    names = [];
    for i in range(len(items)):
        names.append([items[i]['name'], ("Private" if (items[i]['private']) else "Public")])
    return names
    #return items


def main():
    #print(basicAPICall(""))
    print("Public repo names for", user, "\n", getUserPublicRepos(), "\n")
    print("All repo names and privacy status for", user, "\n",getUserAllRepos())

main()
