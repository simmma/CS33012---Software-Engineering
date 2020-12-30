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

def getUserAllRepos():
    if token == "":
        print("Please enter a valid token!")
        return 
    resp = requests.get(url + "search/repositories?q=user:" + user, auth=(user, token))
    if(checkStatus(resp)):
        return ""
    return resp


def main():
    # get data for initial attempt at visualisation
    raw_data = getUserAllRepos().json()["items"]
    data = json.dumps(raw_data[2], indent = 4)

    # Writing to data set file
    with open("Github-Visualisation\data.json", "w") as dataset: # doesn't need the directory specified when run in cmd, VS Code needs it????
        dataset.write(data)
    dataset.close()

main()