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
    resp = requests.get(
        url + "search/repositories?q=user:" + user, auth=(user, token))
    if(checkStatus(resp)):
        return ""
    return resp

def main():
    print("Called userDisplay")
    # Get personal access token (this file is hiden using .gitignore)
    with open("PAT.txt", "r") as tokenFile:
        global token
        token = tokenFile.read()
    tokenFile.close()

    # Get user and repo_name for API query
    with open("repoRef.json", "r") as refFile:
        temp = json.load(refFile)
        login = temp["login"]
    refFile.close()

    raw_data = getURLData("users/" + login)
    if raw_data == "":
        print("Error calling Github API")
        #data = "[]"
        return -1
    else:
        raw_data = raw_data.json()
        # extract required data
        data = {}
        data["login"] = raw_data["login"]
        # get avatar
        avatar_data = requests.get(raw_data["avatar_url"]).content
        with open('static/user_avatar.jpg', 'wb') as handler:
            handler.write(avatar_data)
        # get languages
        raw_data = getURLData("users/" + login + "/repos").json() # users/" + login + "/repos"
        repo_list = []
        for i in range(len(raw_data)): # get list of repo_name "simmma/project"
            repo_list.append(raw_data[i]["full_name"])
        # print(repo_list)
        data["languages"] = {}
        for i in range(len(repo_list)):
            raw_data = getURLData("repos/" + repo_list[i] + "/languages").json()
            lang_list = list(raw_data.keys())
            #print(type(lang_list))
            for j in range(len(lang_list)):
                if lang_list[j] in data["languages"]:
                    data["languages"][lang_list[j]] += raw_data[lang_list[j]]
                else:
                    data["languages"][lang_list[j]] = raw_data[lang_list[j]]
    return 0

main()
