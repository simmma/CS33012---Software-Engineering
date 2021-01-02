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

def getURLData(add):
    if token == "":
        print("Please enter a valid token!")
        return 
    resp = requests.get(url + add, auth=(user, token))
    if(checkStatus(resp)):
        return ""
    return resp

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

    with open("Github-Visualisation/repoRef.json", "r") as refFile:
        temp = json.load(refFile)
        login = temp["login"]
        repo_name = temp["repo_name"]
    refFile.close()

    # get data for initial attempt at visualisation
    raw_data = getURLData("repos/" + login + "/" + repo_name + "/" + "contributors").json()

    # extract required data
    data = {}
    for i in range(len(raw_data)):
        key_id = raw_data[i]["login"]
        data[key_id] = {}
        data[key_id]["contributions"] = raw_data[i]["contributions"]
        
    # Writing to data set file
    data = json.dumps(data, indent = 4)
    with open("Github-Visualisation\df_contrib.json", "w") as dataset: # doesn't need the directory specified when run in cmd, VS Code needs it????
        dataset.write(data)
    dataset.close()

main()