from flask import Flask

from task_url import url_link
from task_html import html_text


app = Flask(__name__)


url_prefix = 'http://127.0.0.1:5000'
if url_link.startswith(url_prefix):
    route = url_link[len(url_prefix)]
else:
    raise ValueError(f'Первая часть ссылки должна быть {url_prefix}')


@app.route(route)
def index():
    return html_text
