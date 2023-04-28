#  Задача: URL
#
#  Напишите программу, которая собирает URL ссылку из компонентов
#  1. Программа спрашивает безопасный ли протокол. Если да, используйте префикс https, иначе http
#  2. Программы спрашивает есть ли у сайта название, оно вводится. Иначе программа запрашивает IP-адрес и порт
#  3. Далее программа запрашивает путь и выводит готовую URL собранную из компонентов
#  4. Готовую URL ссылку нужно хранить в переменной url_link (позже вы узнаете зачем)
#
#  Пример №1:
#
#  Is protocol secure? [y/n]: y
#  Has site name? [y/n]: y
#  Enter site name: wikipedia.org
#  Enter site routing: /wiki/URL
#
#  Your URL: https://wikipedia.org/wiki/URL
#
#  Пример №2:
#
#  Is protocol secure? [y/n]: n
#  Has site name? [y/n]: n
#  Enter IP-address: 127.0.0.1
#  Enter port: 5000
#  Enter site routing: /get
#
#  Your URL: http://127.0.0.1:5000/get

url_link = ...
