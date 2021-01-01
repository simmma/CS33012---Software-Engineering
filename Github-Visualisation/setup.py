# python -m pip install requests
import requests
import json

url = "https://api.github.com/"
user = "simmma"
token = ""

def checkStatus(resp):
    if resp.status_code != 200:
        print("oops")
        print(resp.json()["message"])
        return -1
    return 0

def getUserAllRepos():
    if token == "":
        print("Please enter a valid token!")
        return 
    resp = requests.get(url + "search/repositories?q=user:" + user, auth=(user, token))
    if(checkStatus(resp)):
        return ""
    return resp


def main():
    # Get personal access token (this file is hiden using .gitignore)
    with open("Github-Visualisation\PAT.txt", "r") as tokenFile:
        global token
        token = tokenFile.read()
    tokenFile.close()

    # get data for initial attempt at visualisation
    raw_data = getUserAllRepos().json()
    data = json.dumps(raw_data, indent = 4)

    # extract required data
    items_data = raw_data["items"]
    data = {}
    for i in range(raw_data["total_count"]):
        item_data = items_data[i]
        key_id = item_data["id"]
        data[key_id] = {}
        data[key_id]["name"] = item_data["name"]
        data[key_id]["privacy"] = ("Private" if (item_data["private"]) else "Public")
    print(data)
    
    # Writing to data set file
    data = json.dumps(data, indent = 4)
    with open("Github-Visualisation\data.json", "w") as dataset: # doesn't need the directory specified when run in cmd, VS Code needs it????
        dataset.write(data)
    dataset.close()

main()