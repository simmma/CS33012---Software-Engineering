import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import json
def frmt(x):
    return '{:.0f}'.format(x*total_commits/100)

plt.style.use("seaborn-pastel") # dark_background

# read in data.json
data = pd.read_json("Github-Visualisation\TestDump\df_contrib.json")
data = data.transpose()

# read in source of data
with open("Github-Visualisation/repoRef.json", "r") as refFile:
    temp = json.load(refFile)
    login = temp["login"]
    repo_name = temp["repo_name"]
refFile.close()

# create simple pie chart of number of contributions to a repo
#   format and save pie chart
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
total_commits = (sum(data["contributions"]))
min_commit = round(total_commits/100)
usernames = ["contibution from users with \n" + str(min_commit) + (" commit" if (min_commit == 1) else " or less commits")]
no_contrib = [0]
for i in range(len(data)):
    if(data["contributions"][i] <= min_commit):
        no_contrib[0] += 1
    else:
        usernames.append(data.index[i])
        no_contrib.append(data["contributions"][i])

colours = ["#89023e","#cc7178","#FFADB0","#f3e1dd","#c7d9b7","#95adb6","#ECDCB0","#e5f77d","#82d4bb"]
# Add check for repeated colours ####
ax.pie(no_contrib, labels = usernames, autopct=frmt, shadow = 'true', colors = colours)
plt.title('Comparison of contributions on repo at ' + login + '/' + repo_name + '/')
plt.text(0, 1.2, ("total number of commits: " + str(total_commits)), ha = 'center')
plt.savefig('Github-Visualisation\TestDump\ContribPie.png',dpi=300,bbox_inches='tight') 
plt.show()