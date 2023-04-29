from flask import Flask

print('Form url...\n')
from task_url import url_link
print('Create HTML...\n')
from task_html import html_text


app = Flask(__name__, static_url_path='', static_folder='images')


url_prefix = 'http://127.0.0.1'
if url_link.startswith(url_prefix):
    url_postfix = url_link[len(url_prefix):]
    port = url_postfix[1: url_postfix.index('/')]
    if not port.isnumeric():
        raise ValueError('Номер порта сформирован некорректно. '
                         'Возможно задача решена неправильно или '
                         'порт задан не в том формате')
    route = url_postfix[url_prefix.index('/'):]
else:
    raise ValueError(f'Первая часть ссылки должна быть {url_prefix}')


@app.route(route)
def index():
    return html_text


if __name__ == '__main__':
    app.run(port=port)
