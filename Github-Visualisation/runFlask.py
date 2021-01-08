from flask import Flask, render_template
from userDisplay import main as userDisplay
from repoDisplay import main as repoDisplay

app = Flask(__name__)

def reset():
    data = '{\n\t"login": "",\n\t"repo_name": ""\n}'
    with open("repoRef.json", "w") as dataset:
        dataset.write(data)
    dataset.close()

@app.route('/')
def home():
    return "hello"
@app.route('/<login>')
def userPage(login=""):
    data = '{\n\t"login": "' + login + '",\n\t"repo_name": ""\n}'
    with open("repoRef.json", "w") as dataset:
        dataset.write(data)
    dataset.close()
    #call user setup and visual
    if(userDisplay()):
        return render_template('user404Page.html', login=login)
    else:
        return render_template('userPage.html', login=login)
@app.route('/<login>/<repo_name>')
def repoPage(login="", repo_name=""):
    data = '{\n\t"login": "' + login + '",\n\t"repo_name": "' + repo_name + '"\n}'
    with open("repoRef.json", "w") as dataset:
        dataset.write(data)
    dataset.close()
    if(repoDisplay()):
        return render_template('repo404Page.html', login=login, repo_name=repo_name)
    else:
        return render_template('repoPage.html', login=login, repo_name=repo_name)