from flask import Flask, render_template
from setup import main as setupMain
from Visual import main as visualMain

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
@app.route('/<login>/<repo_name>')
def hello(login="", repo_name=""):
    data = '{\n\t"login": "' + login + '",\n\t"repo_name": "' + repo_name + '"\n}'
    with open("repoRef.json", "w") as dataset:
        dataset.write(data)
    dataset.close()
    setupMain()
    visualMain()
    return render_template('repoPage.html', login=login, repo_name=repo_name)