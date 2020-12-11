import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url = url)
if r.status_code == 200:
    print("Requests Succeed!")

# store API response in a variable.
response_dict = r.json()
repos_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repos_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# make visualization
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend = False)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names

chart.add(title='', values = stars)
chart.render_to_file(filename="Python_repos.svg")