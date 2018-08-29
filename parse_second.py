stroka="1и5в4ыfjgkjadsg45674537hfkjsdgfk676573hfjdjsf90900jfdh"
stroka2="teyrt7658236587fhdj734hjhhj9999"
stroka3="7321878244612476127461286481641286"
stroka4="kjkhfjahdskjgahskljghkasjhgkjah"

# определение числового значения символа из кодировки
#print(ord(stroka[0]))
# какой символ хранится в кодировки с данным числовым значением
#print(chr(666))
#скинуть ссылки на регулярки
#для начала https://python-scripts.com/import-re-regular-expression
import re
pars = re.findall('\d+', stroka)
print(pars)
