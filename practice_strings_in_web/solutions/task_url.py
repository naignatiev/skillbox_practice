# В переменную url по очереди будут добавляться нужные компоненты
# Изначально она пустая
url = ''
# Запрашиваем протокол
is_protocol_secure = input('Is protocol secure? [y/n]: ')
# Если 'y' добавляем https, если 'n'
if is_protocol_secure == 'y':
    url += 'https://'
elif is_protocol_secure == 'n':
    url += 'http://'
# Запрашиваем имя сайта
has_site_name = input('Has site name? [y/n]: ')
# Если у сайта есть имя, спрашиваем его
if has_site_name == 'y':
    url += input('Enter site name: ')
# Иначе спрашиваем IP-адрес и порт
elif has_site_name == 'n':
    url += input('Enter IP-address: ')
    url += ':' + input('Enter port: ')
# Вводим путь, по которому будет доступна страница
url += input('Enter site routing: ')
# Печатаем ответ
print('Your URL:', url)
