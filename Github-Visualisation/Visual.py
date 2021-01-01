import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use("seaborn") # dark_background

# read in data.json
data = pd.read_json("Github-Visualisation\data.json")
data = data.transpose()

# create simple pie chart of ratio of private to public repos in data.json
#   tally private versus public repos
pri_count = 0
pub_count = 0
for i in range(data.shape[0]):
    if(data["privacy"][i] == "Private"):
        pri_count += 1
    elif(data["privacy"][i] == "Public"):
        pub_count += 1

#   format and save pie chart
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
privacies = ["Public", "Private"]
tally = [pub_count, pri_count]
ax.pie(tally, labels = privacies, autopct='%1.2f%%')
plt.title('Ratio of public to private repos')
plt.savefig('Github-Visualisation\Img\pieImage.png',dpi=300,bbox_inches='tight') 
# plt.show()