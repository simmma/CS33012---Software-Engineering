import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import json

total_commits = 1;

def main():
    print("Called main() from Visual.py")
    plt.style.use("seaborn-pastel") # dark_background

    # read in data.json
    data = pd.read_json("df_contrib.json")
    if data.empty: # Update image too??
        print("No data to graph")
        return

    # read in source of data
    with open("repoRef.json", "r") as refFile:
        temp = json.load(refFile)
        login = temp["login"]
        repo_name = temp["repo_name"]
    refFile.close()

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

def frmt(x):
    global total_commits
    return '{:.0f}'.format(x*(total_commits)/100)

main()