from flask import Flask

print('Form url...\n')
from task_url import url_link
print('Create HTML...\n')
from task_html import html_text


app = Flask(__name__, static_url_path='', static_folder='images')


url_prefix = 'http://127.0.0.1:5000'
if url_link.startswith(url_prefix):
    route = url_link[len(url_prefix):]
else:
    raise ValueError(f'Первая часть ссылки должна быть {url_prefix}')


@app.route(route)
def index():
    return html_text


app.run()
