import json
import requests

# https://api.github.com/
# Нас интересует - "user_repositories_url": "https://api.github.com/users/{user}/repos{?type,page,per_page,sort}",

user = 'serg-myst'
url = f'https://api.github.com/users/{user}/repos'

repo_path = requests.get(url)
if repo_path.status_code != 200:
    print(f'Нет репозиториев у пользователя {user}')
else:
    repo_list = json.loads(repo_path.content.decode('utf8'))
    user_repos = []
    for repo_dict in repo_list:
        user_repos.append({'name': repo_dict['name']})
    with open('../user_repos.txt', 'w', encoding='utf-8') as outfile:
        json.dump(user_repos, outfile)
