# 4. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Грустная история абвгдеёжз. Однажды аававаБвв утром я абвввыф пошел ыфвабвфыв на работу. Мне ааабвбфыв это не особо абвва понравилось абвфыв (( АБВГД! Абв Конец!'

new_text = ' '.join(list(x for x in text.split(' ') if not 'абв' in x.lower()))
print(new_text)