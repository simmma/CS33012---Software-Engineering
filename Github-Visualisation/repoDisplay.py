# python -m pip install requests
import requests
import json
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

total_commits = 1;
url = "https://api.github.com/"
user = "simmma"
token = ""

def frmt(x):
    global total_commits
    return '{:.0f}'.format(x*(total_commits)/100)

def checkStatus(resp):
    if resp.status_code != 200:
        print("checkStatus Error:", resp.json()["message"])
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
    print("Called repoDisplay")
    # Get personal access token (this file is hiden using .gitignore)
    with open("PAT.txt", "r") as tokenFile:
        global token
        token = tokenFile.read()
    tokenFile.close()

    # Get user and repo_name for API query
    with open("repoRef.json", "r") as refFile:
        temp = json.load(refFile)
        login = temp["login"]
        repo_name = temp["repo_name"]
    refFile.close()

    data = list()
    # get data for contributions
    raw_data = getURLData("repos/" + login + "/" + repo_name + "/" + "contributors")
    if raw_data == "":
        print("Error calling Github API")
        return -1
    else:
        raw_data = raw_data.json()
        # extract required data
        for i in range(len(raw_data)):
            data.append({})
            data[i]["login"] = raw_data[i]["login"]
            data[i]["contributions"] = raw_data[i]["contributions"]
        data = json.dumps(data, indent=4)

    plt.style.use("seaborn-pastel") # dark_background      
    # read in data.json
    if not data: # Update image too??
        print("No data to graph")
        return

    data = pd.read_json(data)

    # create simple pie chart of number of contributions to a repo
    #   format and save pie chart
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.axis('equal')
    global total_commits 
    total_commits = (sum(data["contributions"]))
    min_commit = round(total_commits/100)
    usernames = ["contibution from users with \n" + str(min_commit) + (" commit" if (min_commit == 1) else " or less commits")]
    no_contrib = [0]
    for i in range(len(data)):
        if(data["contributions"][i] <= min_commit):
            no_contrib[0] += 1
        else:
            usernames.append(data["login"][i])
            no_contrib.append(data["contributions"][i])

    # if there were no commits below threshold
    if no_contrib[0] == 0:
        no_contrib.pop(0)
        usernames.pop(0)

    colours = ["#89023e","#cc7178","#FFADB0","#f3e1dd","#c7d9b7","#95adb6","#ECDCB0","#e5f77d","#82d4bb"]
    # Add check for repeated colours ####
    ax.pie(no_contrib, labels = usernames, autopct=frmt, shadow = 'true', colors = colours)
    plt.title('Comparison of contributions on repo at ' + login + '/' + repo_name + '/')
    plt.text(0, 1.2, ("total number of commits: " + str(total_commits)), ha = 'center')
    plt.savefig('static\ContribPie.png',dpi=300,bbox_inches='tight') 
    #plt.show()
    return 0
main()
