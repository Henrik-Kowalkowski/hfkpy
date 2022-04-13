import requests
import json
import pathlib
import pandas as pd

# Get the dynamic path to the file so we can edit the tests in interactive mode
# Need to put hfkpy on the python path to get this to work without pathlib
ROOT_DIR = str(pathlib.Path(__file__).parents[1])

tokens = pd.read_csv(pathlib.Path(ROOT_DIR) / "tokens.csv")
token = tokens.loc[tokens.group == "github", "token_id"].item()
git_api = "https://api.github.com"
username = "Henrik-Kowalkowski"
repo = "hfkpy"


url = f"{git_api}/users/{username}"
requests.get(url).text

url = f"{git_api}/repos/{username}/{repo}/traffic/views"
requests.get(url, auth=(username, token)).text

url = f"{git_api}/repos/{username}/{repo}/releases/latest"
requests.get(url, auth=(username, token)).text

url = f"{git_api}/repos/{username}/{repo}/git/refs/tags"
json.loads(requests.get(url, auth=(username, token)).text)

url = f"{git_api}/repos/{username}/{repo}/stats/code_frequency"
json.loads(requests.get(url).text)

url = f"{git_api}/repos/{username}/{repo}/stats/commit_activity"
json.loads(requests.get(url, auth=(username, token)).text)

url = f"{git_api}/repos/{username}/{repo}/releases?/per_page=100"
releases = json.loads(requests.get(url, auth=(username, token)).text)

for rel in releases:
  if rel['assets']:
    tag = rel['tag_name']
    dls = rel['assets'][0]['download_count']
    pub = rel['published_at']
    print(f"Pub: {pub} | Tag: {tag} | Dls: {dls} ")