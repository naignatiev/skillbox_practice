# Вводится заголовок сайта
title_name = input('Enter title name: ')
# Вводится текст страницы
text = input('Enter text: ')
# Вводится название файла изображения из папки images.
# Название должно указываться с расширением. Например: cat.jpg, а не cat
image_path = input('Enter image path: ')
# Заголовок страницы оборачивается в тэг <title>
title_tag = '<title>' + title_name + '</title>'
# Текст страницы оборачивается в тэг <p>
text_tag = '<p>' + text + '</p>'
# В одинарный блок <img> в атрибут src="", вставляется путь до картинки
image_tag = '<img src="' + image_path + '">'
# Собирается html. Между блоками расставляются переносы строки
html_text = title_tag + '\n' + text_tag + '\n' + image_tag
# Вывод с отделением сообщения Your HTML сверху и снизу переносом строки
print('\nYour HTML:\n', html_text)
